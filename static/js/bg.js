includeHTML = async () => {
    const element = document.body.querySelector(".bg-animated");
    // console.log(element);
    const file = element.getAttribute("include-html");
    // console.log(file);
    const data = await fetch(file).then((respose) => respose.text());
    console.log(data);
    element.innerHTML = data;
  };
  
  