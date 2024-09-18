
    const openList = document.querySelector(".Open_List");
    const list = document.querySelector("nav .Options_Site_Name .List");
    const icon = document.querySelector(".Open_List i");

    openList.addEventListener("click", () => {
        if (list.style.display === "block") {
            list.style.height = "0";
            list.style.display = "none";
        } else {
            list.style.display = "block";
            list.style.height = "auto";
            var height = list.scrollHeight;
            list.style.height = "0";
            setTimeout(() => {
                list.style.height = height + "px";
                list.style.transition = "height 0.5s";
            }, 1);
        }
        icon.classList.toggle("rotate");
    });

    openList.addEventListener("click", () => {
        if (list.classList.contains("show")) {
            list.classList.remove("show");
            list.classList.add("hide");
        } else {
            list.classList.remove("hide");
            list.classList.add("show");
        }
        icon.classList.toggle("rotate");
    });

    let profileDropdownList = document.querySelector(".profile-dropdown-list");
    let btn = document.querySelector(".profile-dropdown-btn");

    let classList = profileDropdownList.classList;

    const toggle = () => classList.toggle("active");

    window.addEventListener("click", function (e) {
        if (!btn.contains(e.target)) classList.remove("active");
    });