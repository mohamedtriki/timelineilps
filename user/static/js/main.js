window.addEventListener('load',function(){
    var tl = gsap.timeline();
    tl.to(".dot-wave",{opacity:0,duration:0.7})
    tl.to("#preloader",{opacity:0,duration:0.7})    
    tl.to("#preloader",{display:'none'})     
    tl.to(document.getElementsByTagName('html')[0],{overflowY:'scroll'},'-=1.2')     

})








const titles = document.querySelectorAll('.event_title');

titles.forEach((title) => {
  title.addEventListener('click', () => {

    const eventDesc = title.nextElementSibling;
    const innerElement = title.querySelector('.expend_arrow');
    eventDesc.classList.toggle('active');


    if (eventDesc.offsetHeight  !== 0) {
        const angle = 0;
        innerElement.setAttribute("transform", "rotate(0)");

        innerElement.style.transition = "transform 0.5s ease-in-out";
        
        innerElement.style.transformOrigin = "center";
        
        setTimeout(() => {
          innerElement.setAttribute("transform", `rotate(${angle})`);
        }, 10);
      } 
    else {
        const angle = -180;
        innerElement.setAttribute("transform", "rotate(0)");

        innerElement.style.transition = "transform 0.5s ease-in-out";
        
        innerElement.style.transformOrigin = "center";
        
        setTimeout(() => {
          innerElement.setAttribute("transform", `rotate(${angle})`);
        }, 10);
      }

  });
});



const scrollTrigger = document.getElementById("subscribe");
scrollTrigger.addEventListener("click", scrollToElement);

function scrollToElement() {
  const elementToScrollTo = document.getElementById("footer");
  elementToScrollTo.scrollIntoView({ behavior: "smooth" });
}







