Code Quest
============

## Roadmap
1. Game Design
 * What's the goal?
     * Get to the end of the dungeon with the highest score
	 * Score determined by time and enemies defeated
	 * high scores stored per file (md5 checksum to identify file content)
 * What does a player do in each room?
     * Get to next room
	 * Defeat enemies
	 * TODO
 * What room elements are controlled by source parsing?
     * Enemy type and number
	 * Room connections
	 * Room type
	      * Defeat all enemies to pass
		  * Find switch
		  * TODO
     * TODO
2. XML Design
 * Research designing custom XML schema
     * Create an .xsd file, which describes the schema
	 * can validate with [lxml](http://lxml.de/validation.html#xmlschema)
 * Research best practices
 * Dungeon Design
     * single dungeon tag containing rooms
     * How to connect/relate rooms?
     * What attributes will rooms need?
     * What attributes will the dungeon need as a whole?
3. Python parsing adapter
 * Make abstract enough that any adapter that produces dungeon XML can be used
 * For now, handle only single source files
 * Choose Python XML module: [built-in possibilities](https://docs.python.org/2/library/xml.html#module-xml)
     * [lxml](http://lxml.de/) supports xsd validation, so use this
 * Use [ast module](https://docs.python.org/3.3/library/ast.html) to generate tree from source
 * Parse converted source into dungeon XML
     * Create Dungeon/Room objects, then serialize into XML?
     * Create straight into XML and deserialize into objects later?
 * Research possibilities of malicious XML generation
     * [info for built-in xml module](https://docs.python.org/2/library/xml.html#xml-vulnerabilities)
4. Game Side
 * Engine
     * Pyglet
 * Dungeon Interpreter
     * Given dungeon XML, convert to Dungeon object
     * Serialize straight into Dungeon object possible?
