var BubbleShoot = window.BubbleShoot || {};
BubbleShoot.Game = (function($){
	var Game = function(){
		var curBubble;
		var board;
		var numBubbles;
		var bubbles = [];
		var MAX_BUBBLES = 70;
		var POINTS_PER_BUBBLE = 50;
		var level = 0;
		var score = 0;
		var highScore = 0;
		var requestAnimationID;
		var MAX_ROWS = 11;
		this.init = function(){
			if(BubbleShoot.Renderer){
				BubbleShoot.Renderer.init(function(){
					$(".but_start_game").click("click",startGame);
				});
			}else{
				$(".but_start_game").click("click",startGame);
			};
			if(window.localStorage && localStorage.getItem("high_score")){
				highScore = parseInt(localStorage.getItem("high_score"));
			}
			BubbleShoot.ui.drawHighScore(highScore);
		};
		var startGame = function(){
			$(".but_start_game").unbind("click");
			numBubbles = MAX_BUBBLES - level * 5;;
			BubbleShoot.ui.hideDialog();
			board = new BubbleShoot.Board();
			bubbles = board.getBubbles();
			if(BubbleShoot.Renderer)
			{
				if(!requestAnimationID)
					requestAnimationID = requestAnimationFrame(renderFrame);
			}else{
				BubbleShoot.ui.drawBoard(board);
			};
			curBubble = getNextBubble();
			$("#game").bind("click",clickGameScreen);
			BubbleShoot.ui.drawScore(score);
			BubbleShoot.ui.drawLevel(level);
		};
		var getNextBubble = function(){
			var bubble = BubbleShoot.Bubble.create();
			bubbles.push(bubble);
			bubble.setState(BubbleShoot.BubbleState.CURRENT);
			bubble.getSprite().addClass("cur_bubble");
			var top = 470;
			var left = ($("#board").width() - BubbleShoot.ui.BUBBLE_DIMS)/2;
			bubble.getSprite().css({
				top : top,
				left : left
			});
			$("#board").append(bubble.getSprite());
			BubbleShoot.ui.drawBubblesRemaining(numBubbles);
			numBubbles--;
			return bubble;
		};
		var clickGameScreen = function(e){
			var angle = BubbleShoot.ui.getBubbleAngle(curBubble.getSprite(),e);
			var duration = 750;
			var distance = 1000;
			var collision = BubbleShoot.CollisionDetector.findIntersection(curBubble,
				board,angle);
			if(collision){
				var coords = collision.coords;
				duration = Math.round(duration * collision.distToCollision / distance);
				board.addBubble(curBubble,coords);
				var group = board.getGroup(curBubble,{});
				if(group.list.length >= 3){
					popBubbles(group.list,duration);
					var topRow = board.getRows()[0];
					var topRowBubbles = [];
					for(var i=0;i<topRow.length;i++){
						if(topRow[i])
							topRowBubbles.push(topRow[i]);
					};
					if(topRowBubbles.length <= 5){
						popBubbles(topRowBubbles,duration);
						group.list.concat(topRowBubbles);
					};
					var orphans = board.findOrphans();
					var delay = duration + 200 + 30 * group.list.length;
					dropBubbles(orphans,delay);
					var popped = [].concat(group.list,orphans);
					var points = popped.length * POINTS_PER_BUBBLE;
					score += points;
					setTimeout(function(){
						BubbleShoot.ui.drawScore(score);
					},delay);
				}
			}else{
				var distX = Math.sin(angle) * distance;
				var distY = Math.cos(angle) * distance;
				var bubbleCoords = BubbleShoot.ui.getBubbleCoords(curBubble.getSprite());
				var coords = {
					x : bubbleCoords.left + distX,
					y : bubbleCoords.top - distY
				};
			};
			BubbleShoot.ui.fireBubble(curBubble,coords,duration);
			if(board.getRows().length > MAX_ROWS){
				endGame(false);
			}else if(numBubbles == 0){
				endGame(false);
			}else if(board.isEmpty()){
				endGame(true);
			}else{
				curBubble = getNextBubble(board);
			}
		};
		var popBubbles = function(bubbles,delay){
			$.each(bubbles,function(){
				var bubble = this;
				setTimeout(function(){
					bubble.setState(BubbleShoot.BubbleState.POPPING);
					bubble.animatePop();
					setTimeout(function(){
						bubble.setState(BubbleShoot.BubbleState.POPPED);
					},200);
					BubbleShoot.Sounds.play("_mp3/pop.mp3",Math.random()*.5 + .5);
				},delay);
				board.popBubbleAt(this.getRow(),this.getCol());
				setTimeout(function(){
					bubble.getSprite().remove();
				},delay + 200);
				delay += 60;
			});
		};
		var dropBubbles = function(bubbles,delay){
			$.each(bubbles,function(){
				var bubble = this;
				board.popBubbleAt(bubble.getRow(),bubble.getCol());
				setTimeout(function(){
					bubble.setState(BubbleShoot.BubbleState.FALLING);
					bubble.getSprite().kaboom({
						callback : function(){
							bubble.getSprite().remove();
							bubble.setState(BubbleShoot.BubbleState.FALLEN);
						}
					})
				},delay);
			});
		};
		var renderFrame = function(){
			$.each(bubbles,function(){
				if(this.getSprite().updateFrame)
					this.getSprite().updateFrame();
			});
			BubbleShoot.Renderer.render(bubbles);
			requestAnimationID = requestAnimationFrame(renderFrame);
		};
		var endGame = function(hasWon){
			if(score > highScore){
				highScore = score;
				$("#new_high_score").show();
				BubbleShoot.ui.drawHighScore(highScore);
				if(window.localStorage){
					localStorage.setItem("high_score",highScore);
				}
			}else{
				$("#new_high_score").hide();
			};
			if(hasWon){
				level++;
			}else{
				score = 0;
				level = 0;
			};
			$(".but_start_game").click("click",startGame);
			$("#board .bubble").remove();
			BubbleShoot.ui.endGame(hasWon,score);
		};
	};
	window.requestAnimationFrame = Modernizr.prefixed("requestAnimationFrame",
		window) || function(callback){
		window.setTimeout(function(){
			callback();
		}, 40);
	};
	return Game;
})(jQuery);