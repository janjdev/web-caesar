const textarea = document.getElementsByTagName('textarea')[0];
textarea.addEventListener('focus', function(){

    this.value = '';

})