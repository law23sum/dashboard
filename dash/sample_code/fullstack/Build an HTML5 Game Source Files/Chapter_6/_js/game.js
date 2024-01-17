var BubbleShoot = window.BubbleShoot || {};
BubbleShoot.Game = (function($){
	var Game = function(){
		var curBubble;
		var board;
		var numBubbles;
		var bubbles = [];
		var MAX_BUBBLES = 70;
		var requestAnimationID;
		this.init = function(){
			if(BubbleShoot.Renderer){
				BubbleShoot.Renderer.init(function(){
					$(".but_start_game").click("click",startGame);
				});
			}else{
				$(".but_start_game").click("click",startGame);
			};
		};
		var startGame = function(){
			$(".but_start_game").unbind("click");
			numBubbles = MAX_BUBBLES;
			BubbleShoot.ui.hideDialog();
			board = new BubbleShoot.Board();
			bubbles = board.getBubbles();
			curBubble = getNextBubble();
			if(BubbleShoot.Renderer)
			{
				if(!requestAnimationID)
					requestAnimationID = setTimeout(renderFrame,40);
			}else{
				BubbleShoot.ui.drawBoard(board);
			};
			$("#game").bind("click",clickGameScreen);
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
					var orphans = board.findOrphans();
					var delay = duration + 200 + 30 * group.list.length;
					dropBubbles(orphans,delay);
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
			curBubble = getNextBubble();
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
			requestAnimationID = setTimeout(renderFrame,40);
		};
	};
	return Game;
})(jQuery);