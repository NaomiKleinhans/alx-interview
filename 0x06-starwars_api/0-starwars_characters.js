#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
	console.error('Please provide a Movie ID as an argument.');
	process.exit(1);
}

const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request(url, (error, response, body) => {
	if (error) {
		console.error('Error:', error);
		return;
	}

	const data = JSON.parse(body);
	const characters = data.characters;

	const fetchCharacter = (url) =>
		new Promise((resolve, reject) => {
			request(url, (error, response, body) => {
				if (error) reject(error);
				else resolve(JSON.parse(body).name);
			});
		});

	(async () => {
		for (const characterUrl of characters) {
			try {
				const characterName = await fetchCharacter(characterUrl);
				console.log(characterName);
			} catch (error) {
				console.error('Error fetching character:', error);
			}
		}
	})();
});
