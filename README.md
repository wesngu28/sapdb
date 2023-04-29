# Super Auto Pets Browser & DB

WIP project that aims to scrape data regarding Super Auto Pets from the wiki and then offer a REST api as well as a frontend interface using views that consumes the API and  allows you to filter them.

Feature Plan

API
- [ ] Plan out models for animals, foods, and packs
- [ ] Include a table and join table for something like archetypes and actual effects. An archetype defines how a food or animal is actually used. For example, a whale is primarily used in the summon or faint archetype where you want it to kill a unit with a good faint, but its actual effect is as start of battle so its also bought in conjunction with a salamander. I probably want to make two tables for this.
 - Food is also something to consider here, since food can have overlapping archeyptal usecase and effects, but I don't know if it's worth considering food and animal archetype and effects separate. Leaning no.
- [ ] Make the routes include parameter for the archetype and effects when done.
- [ ] Do something with the photos, I can either download them and store them in a CDN, in the repo in a static folder, or just use wiki or assets or similar solution.
- [ ] Make a command to make updating through scraping the website or manually inputting data easier.

View
- [ ] Consider if I want to use templates or front-end framework. Templates seem to do what I want fine but maybe want SPA performance
- [ ] Consider using UI library
