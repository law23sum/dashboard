var BubbleShoot = window.BubbleShoot || {};
BubbleShoot.Bubble = (function($){
	var Bubble = function(sprite){
		var that = this;
		this.getSprite = function(){ return sprite;};
	};
	Bubble.create = function(){
		var sprite = $(document.createElement("div"));
		sprite.addClass("bubble");
		sprite.addClass("bubble_0");
		var bubble = new Bubble(sprite);
		return bubble;
	};
	return Bubble;
})(jQuery);