# Planned server API routes

- GET `/home`: landing page. quick summary of cold iron (dump this once react app setup? unsure)
- POST `/login`: accepts a payload of username (str), hashed password (str)
- GET `/characters/user/<userid>`: returns list of characters belonging to the user. full character object?
- GET `/characters/<charid>`: returns a single character sheet
- POST `/characters/<charid>`: updates a single character sheet, accepts a payload something like:
    - `character: <character object>`
    - `password: <logged in user hashed password>`
    - seems overkill but want to avoid other users overwriting other user pws
- POST `/characters/create`: adds a new blank character to the database under the given user
- GET `/items?category=<blarg>`: returns list of all items in the game. optional `category` query parameter.

# Planned pages on frontend app
- `/characters`: renders list of all characters belonging to the logged in user.
- `/items`: a rendered table of the items in the game. top bar has category selectors.
    - `[weapons, armor, misc]` etc. an option to display all.
    - search bar to filter table entries by name.
    - sortable columns.
    - where applicable, items with traits have them in a tooltip on hover.
- `/rules`: the rules for playing the game.
- `/lore`: the flavor around the rules for playing the game.
