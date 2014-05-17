Code Quest
============

## Roadmap
1. Game Design
 * What's the goal?
 * What does a player do in each room?
 * What room elements are controlled by source parsing?
2. XML Design
 * Research designing custom XML schema
 * Research best practices
 * Dungeon Design
     * single dungeon tag containing rooms
     * How to connect/relate rooms?
     * What attributes will rooms need?
     * What attributes will the dungeon need as a whole?
3. Python parsing adapter
 * Make abstract enough that any adapter that produces dungeon XML can be used
 * Choose Python XML module: [built-in possibilities](https://docs.python.org/2/library/xml.html#module-xml)
 * Use [ast module](https://docs.python.org/3.3/library/ast.html) to generate tree from source
 * Parse converted source into dungeon XML
     * Create Dungeon/Room objects, then serialize into XML?
     * Create straight into XML and deserialize into objects later?
 * Research possibilities of malicious XML generation
     * [info for built-in xml module](https://docs.python.org/2/library/xml.html#xml-vulnerabilities)
4. Game Side
 * Engine
     * Pygame vs. Pyglet
 * Dungeon Interpreter
     * Given dungeon XML, convert to Dungeon object
     * Serialize straight into Dungeon object possible?
