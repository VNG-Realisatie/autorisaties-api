var path = require('path');
var fs = require('fs');


/** Parses package.json */
var pkg = JSON.parse(fs.readFileSync('./package.json', 'utf-8'));

/** Name of the sources directory */
var sourcesRoot = `src/${pkg.name}/`;

/** Name of the static (source) directory */
var staticRoot = `${sourcesRoot}static/`;


/**
 * Application path configuration for use in frontend scripts
 */
module.exports = {
    // Parsed package.json
    package: pkg,

    // Path to the sass (sources) directory
    scssSrcDir: `${sourcesRoot}sass/`,

    // Path to the sass (sources) entry point
    scssEntry: `${sourcesRoot}sass/screen.scss`,

    // Path to the (transpiled) css directory
    jsDir: `${staticRoot}bundles/`,

    // Path to the fonts directory
    fontsDir: `${staticRoot}fonts/`
};
