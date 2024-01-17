var BubbleShoot = window.BubbleShoot || {};
BubbleShoot.Bubble = (function($){
	var Bubble = function(row,col,type,sprite){
		var that = this;
		this.getType = function(){ return type;};
		this.getSprite = function(){ return sprite;};
		this.getCol = function(){ return col;};
		this.setCol = function(colIn){ col = colIn;};
		this.getRow = function(){ return row;};
		this.setRow = function(rowIn){ row = rowIn;};
		this.getCoords = function(){
			var coords = {
				left : that.getCol() * BubbleShoot.ui.BUBBLE_DIMS/2 +
				BubbleShoot.ui.BUBBLE_DIMS/2,
				top : that.getRow() * BubbleShoot.ui.ROW_HEIGHT + BubbleShoot.
					ui.BUBBLE_DIMS/2
			};
			return coords;
		}
	};
	Bubble.create = function(rowNum,colNum,type){
		if(type === undefined){
			type = Math.floor(Math.random() * 4);
		};
		var sprite = $(document.createElement("div"));
		sprite.addClass("bubble");
		sprite.addClass("bubble_" + type);
		var bubble = new Bubble(rowNum,colNum,type,sprite);
		return bubble;
	};
	return Bubble;
})(jQuery);