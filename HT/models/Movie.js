const mongoose = require("mongoose");

const Schema = mongoose.Schema;

let moviesSchema = new Schema ({
    name: String,
    year: Number,
    actors: [String],
    genres: [String],
    ratings: [Number]
})

module.exports = mongoose.model("Movie", moviesSchema);