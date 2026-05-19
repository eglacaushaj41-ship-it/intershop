let buttons = document.querySelectorAll(".add-cart");
let cartCount = document.getElementById("cart-count");

let count = 0;

buttons.forEach(btn => {
  btn.addEventListener("click", () => {
    count++;
    if(cartCount){
      cartCount.innerText = count;
    }

    btn.innerText = "Added ✓";

    setTimeout(() => {
      btn.innerText = "Add To Cart";
    }, 1000);
  });
});