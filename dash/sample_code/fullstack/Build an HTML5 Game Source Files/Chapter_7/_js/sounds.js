var BubbleShoot = window.BubbleShoot || {};
BubbleShoot.Sounds = (function(){
	var soundObjects = [];
	for(var i=0;i<10;i++){
		soundObjects.push(new Audio());
	}
	var curSoundNum = 0;
	var Sounds = {
		play : function(url,volume){
		if(Modernizr.audio){
			var sound = soundObjects[curSoundNum];
			sound.src = url;
			sound.volume = volume;
			sound.play();
			curSoundNum++
			if(curSoundNum >= soundObjects.length){
				curSoundNum = curSoundNum % soundObjects.length;
			}
		}
	}
};
return Sounds;
})();