const div1 = document.getElementById("Total")!;
const div2 = document.getElementById("Dispo")!;
const div3 = document.getElementById("Occup")!;


function listTotal()
{
    div1.style.display = "inline";
    div2.style.display = "none";
    div3.style.display = "none";
}

function listDispo()
{
    div1.style.display = "none";
    div2.style.display = "inline";
    div3.style.display = "none";
}

function listOccup()
{
    div1.style.display = "none";
    div2.style.display = "none";
    div3.style.display = "inline";
}