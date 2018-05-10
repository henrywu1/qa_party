var fs = require('fs');

console.log("LUNCH PARRTTTTYYY");

let places = [
    {
      name: 'CALEXICO',
      description: '',
      veggie_options: true,
    },
    {
      name: 'AUGUST GATHERING',
      description: '',
      veggie_options: true,
    },
    {
      name: 'ALIDORO',
      description: '',
      veggie_options: true,
    },
    {
      name: 'SUNRISE MART',
      description: '',
      veggie_options: true,
    },
    {
      name: 'MCDONALDS',
      description: '',
      veggie_options: true,
    },
    {
      name: "BA'ALS",
      description: '',
      veggie_options: true,
    },
  ];

function isPlaceInList(place, list) {
  for (var i = 0; i < list.length; i++) {
    if (list[i].name === place.name) {
      return true;
    }
  }
  return false;
}

/////////////////////////////////////////////////////////////////


let ate_here_already = [];
let DAYS_TO_KEEP = -3;
ate_here_already = require('./ate_here_this_week.json');
ate_here_already = ate_here_already.slice(DAYS_TO_KEEP);

let selected_place = places[Math.floor(Math.random() * places.length)];
let asdf = isPlaceInList(selected_place, ate_here_already);


while (isPlaceInList(selected_place, ate_here_already)) {
  selected_place = places[Math.floor(Math.random() * places.length)];
  asdf = isPlaceInList(selected_place, ate_here_already)
}
console.log("LETS GO EAT AT " + selected_place.name);

ate_here_already.push(selected_place);
ate_here_already = ate_here_already.slice(DAYS_TO_KEEP);
fs.writeFile("ate_here_this_week.json", JSON.stringify(ate_here_already), function(err) {
    if(err) {
        return console.log(err);
    }
    console.log("The file was saved!");
});
