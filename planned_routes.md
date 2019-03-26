# Planned routes

- `/home`: landing page. quick summary of cold iron
- `/login`: login + registration page. on successful submission redirects to home.
- `/characters`: links to character sheets that the user has stored
- `/characters/<charid>`: renders a character sheet for the given character
- `/items`: renders a table of the items registered in the db, top bar has category selectors.
    - `[weapons, armor, misc]` etc. an option to display all.
    - search bar to filter table entries by name.
    - sortable columns.
    - where applicable, items with traits have them in a tooltip on hover.
- `/rules`: the rules for playing the game.
- `/lore`: the flavor around the rules for playing the game.