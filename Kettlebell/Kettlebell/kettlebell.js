function gyakorlatGeneralas() {
    var gyakorlatok = ["Swing", "Magasra húzás", "Serleg guggolás", "Szélmalom", "Török felállás"];
    var gyakorlat = document.getElementById("generaltGyakorlat");
    var ismetles = Math.floor(Math.random() * 30) + 1;
    var gyakorlatIndex =  Math.floor(Math.random() * gyakorlatok.length) + 1;
    gyakorlat.innerText = ismetles + " darab " + gyakorlatok[gyakorlatIndex];
    if (ismetles % 2 == 0) {
        gyakorlat.style.color = "red";
    } else {
        gyakorlat.style.color = "blue";
    }
}