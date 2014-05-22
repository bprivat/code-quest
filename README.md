Code Quest
============

## Roadmap
1. Game Design
 * What's the goal?
     * Get to the end of the dungeon with the highest score
	 * Score determined by time and enemies defeated
 * What does a player do in each room?
     * Get to next room by
	 * defeating enemies
	 * finding switch/key to unlock door
	 * TODO
 * What room elements are controlled by source parsing?
     * Enemy type and number
     * Room connections
     * Room type (goal to continue)
     * TODO
2. XML Design
 * Research designing custom XML schema
     * Create an .xsd file, which describes the schema
	 * can validate with [lxml](http://lxml.de/validation.html#xmlschema)
	 * Create a validator script, so people can easily verify their xml
 * Research best practices
 * Dungeon Design
     * single dungeon tag containing rooms
     * How to connect/relate rooms?
          * Optional N,S,E,W tags containing room IDs?
     * What attributes will rooms need?
          * Unique ID
          * Enemies element describes enemy groups
          * Goal element describes room goal (defeat enemies, unlock, etc)
     * What attributes will the dungeon need as a whole?
          * Starting and ending room IDs
          * sha1 of source content
               * Collision free, so should be able to uniquely identify different sources
               * Can be used as key for high score later
3. Python parsing adapter
 * Make abstract enough that any CQParser subclass can be used
 * For now, handle only single source files
 * Choose Python XML module: [lxml](http://lxml.de/) supports xsd validation, so use this
 * Use [ast module](https://docs.python.org/3.3/library/ast.html) to generate tree from source
 * Parse converted source into dungeon XML
     * Create Dungeon/Room objects, then serialize into XML?
     * Create straight into XML and deserialize into objects later?
 * Research possibilities of malicious XML generation
4. Game Side
 * Engine
     * Pyglet
 * Dungeon Interpreter
     * Validate given xml via xsd file
     * Given dungeon XML, convert to Dungeon object
     * Serialize straight into Dungeon object possible?
5. Execution
 * Launch pyglet window via command line
 * ~~args~~
6. Future Features
 * Persistent high scores
     * What's best? SQLite? Pickle? Something else?
 * Different player character depending on source type
 * Select source code from GUI, get preview stats
