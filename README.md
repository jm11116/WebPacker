## WebPacker
This is a Python script which will allow the easy concatenation of JavaScript in OOP projects where you'd like to follow the one class per file rule. All you have to do is drop your JavaScript classes into folders named after the feature to which they pertain into /source/js (e.g. /source/js/gallery/) and it will join all your individual class files into one, and it will append the contents of a main.js file at the end of the script so that you can write some procedural code to make it all work. Each feature of the web application you are creating should have its own folder, with individual class files inside. The name of the folder containing the class files will become the name of the compiled JavaScript file that results. This eliminates the need for slow and complicated module loaders to keep your source code organized, and reduces the number of HTTP requests the browser needs to make to load all your scripts to just one.

The script also supports the concatenation of CSS files inside /source/css, so you can keep your stylesheets in multiple files instead of a single giant one. This is great for programmers who want to modularize their CSS code in development but want to combine it all into one file for deployment.

The script also allows the optional compression of JavaScript and CSS, something which can be controlled by simply setting one of the two global variables at the top of the script to true or false.

Later versions of the script will include automatic backups of the deployment folder before it is overwritten by the latest version of the compiled code, and a performance monitor which will report file size reductions as a result of compression and compile time statistics when script execution is complete.

Note: jsmin and csscompressor will need to be installed via pip on your machine for the JavaScript and CSS minification functionality to work.
