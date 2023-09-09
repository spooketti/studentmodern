
    document.querySelectorAll(".typewriterText").forEach(header => {
        console.log("bruh")
        header.style.width = `${header.innerText.length}ch`
        })

        let sequence = [38,38,40,40,37,39,37,39,66,65]
    let pos = 0;
document.addEventListener('keydown', function(e) 
  {
  let expected = sequence[pos]
  if(e.keyCode == expected)
  {
    pos++;
    if(pos == 10)
    {
      var am,bm,cm
      function fun() 
      {
         
am="-webkit",bm='transform:rotate(1turn);',cm='transition:4s;';
        document.body.style += am+bm+am+cm+bm+cm
      }
    

  fun();
      setTimeout(() => {
   document.body.style -= am+bm+am+cm+bm+cm
}, "4000") 
      
      
        pos = 0;
      
        }
      
  }
else
  {
    pos = 0;
  }
})