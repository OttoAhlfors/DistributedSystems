var express = require('express');
var router = express.Router();
const User = require("../models/User");
const Movie = require("../models/Movie"); 

// Register
router.get('/reqister', function(req, res) {
  console.log(req.body);

  const username = req.body.username;
  const email = req.body.email;
  const password = req.body.password;

  User.findOne({email: email}).then((user) => {
    console.log(user);
    if (user != null) {
      console.log("User already exists");
      res.send("User already exists");
    } else {
      User.create({
        username: username,
        email: email,
        password: password
      })
      console.log("User created");
      res.send("User created");
    }
  })
})

// Login
router.get('/login', function(req, res) {
  console.log(req.body);

  const email = req.body.email;
  const password = req.body.password;

  User.findOne({email: email}).then((user) => {
    console.log(user)
    if (user.password === password) {
      console.log("User logged in");
      res.send("User logged in")
    } else {
      console.log("Wrong password");
      res.send("Wrong password")
    }
  })

  res.send('respond with a resource');
});

// Add movie
router.get('/addmovie', function(req, res) {
  console.log(req.body)

  const name = req.body.name
  const year = req.body.year
  const actors = req.body.actors
  const genres = req.body.genres
  const ratings = req.body.ratings
  
  Movie.findOne({name: name}).then((movie) => {
    console.log(movie)
    if (movie === null) {
      Movie.create({
        name: name,
        year: year,
        actors: actors,
        genres: genres,
        ratings: ratings
      })
      console.log("Movie added");
      res.send("Movie added")
    } else {
      console.log("Movie already in database");
      res.send("Movie already in database")
    }
  })
})

module.exports = router;