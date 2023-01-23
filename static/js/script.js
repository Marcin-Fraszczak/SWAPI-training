const df = document.querySelector(".dataframe");


if (df) {
    let show = 10;
    let more = 10;

    function showRows() {
        rows.forEach(row => {
            const th = row.querySelector("th");
            if (Number(th.textContent) <= show) {
                row.style.display = "";
            } else {
                row.style.display = "none";
            }
        });
        updateButtons(showLessButton, showMoreButton);
    }

    function showMore(more) {
        if ((more < 0 && show > 10) || (more > 0 && show < rows.length)) {
            show += more;
            showRows();
        }
    }

    function updateButtons(showLessButton, showMoreButton) {
        if (show <= 10) {
            showLessButton.classList.add("disabled");
        } else {
            showLessButton.classList.remove("disabled");
        }
        if (show >= rows.length) {
            showMoreButton.classList.add("disabled");
        } else {
            showMoreButton.classList.remove("disabled");
        }
    }


    df.classList.add("table", "table-striped", "text-center");

    const rows = df.querySelectorAll("tbody > tr");
    const showMoreButton = document.querySelector("#show-more");
    const showLessButton = document.querySelector("#show-less");
    showLessButton.addEventListener("click", e => showMore(-more));
    showMoreButton.addEventListener("click", e => showMore(more));
    showRows();

}