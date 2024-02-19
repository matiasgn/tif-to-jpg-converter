<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TIF to JPG Converter</title>
</head>
<body>
    <h1>TIF to JPG Converter</h1>
    <p>This script converts TIF images with old style JPEG compression to JPG format. It utilizes Python and various libraries to achieve this conversion.</p>

    <h2>Usage</h2>
    <p>To use this script, simply run it from the command line with the following arguments:</p>
    <pre><code>python script.py &lt;path_to_tif_file&gt; &lt;output_directory&gt;</code></pre>

    <h2>Dependencies</h2>
    <p>This script requires the following Python libraries:</p>
    <ul>
        <li><a href="https://scikit-image.org/">scikit-image</a></li>
        <li><a href="https://pypi.org/project/imagecodecs/">imagecodecs</a></li>
        <li><a href="https://pypi.org/project/tifffile/">tifffile</a></li>
    </ul>

    <h2>Functionality</h2>
    <p>The script checks for old style JPEG compression in the TIF image. If detected, it converts the image to JPG format. Otherwise, it leaves the image unchanged.</p>

    <h2>How to Run</h2>
    <p>Make sure you have Python installed on your system. Run the script from the command line as shown in the usage section.</p>

    <h2>Contributing</h2>
    <p>Feel free to contribute to this project by submitting pull requests or reporting issues.</p>

    <h2>License</h2>
    <p>This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for details.</p>
</body>
</html>
