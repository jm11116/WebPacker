import os
import pathlib
from jsmin import jsmin
from csscompressor import compress

#Change working directory to build location:
os.chdir(os.path.dirname(os.path.abspath(__file__)))

js_min = True
css_min = True

class File_Handler:
    def remove_unix(self, array): #Removes hidden UNIX files from list of files
        cleaned_array = []
        for file in array:
            if file.startswith(".") == False:
                cleaned_array.append(file)
        return cleaned_array
    def delete_directory_contents(self, directory_path):
        folder = self.remove_unix(os.listdir(directory_path))
        for file in folder:
            os.unlink(directory_path + file)
    def create_blank_file(self, filepath):
        file = open(filepath, "w") #Opening as write creates a file if doesn't exist
        file.write("")
        file.close()
    def does_directory_exist(self, folder_name, path, create):
        directory = pathlib.Path(path)
        if directory.exists() == False:
            print("- ERROR: " + folder_name + " folder does not exist.")
            if create == True:
                print("- Creating " + folder_name + " at " + path)
                os.mkdir(path)
            else:
                print("- Please create " + folder_name + " at " + path)

class Directory_Handler:
    def __init__(self):
        self.change_working_dir_to_site_root()
        self.root = os.getcwd()
        self.source_folder = self.root + "/source/"
        self.js_source_folder = self.source_folder + "js/"
        self.css_source_folder = self.source_folder + "css/"
        self.deploy_folder = self.root + "/deploy/"
        self.js_deploy_folder = self.deploy_folder + "js/"
        self.packed_css_file = self.deploy_folder + "styles.css"
        files.does_directory_exist("/deploy/", self.deploy_folder, True)
        files.does_directory_exist("/deploy/js/", self.js_deploy_folder, True)
        files.does_directory_exist("/source/", self.source_folder, False)
        files.does_directory_exist("/source/js/", self.js_source_folder, False)
        files.does_directory_exist("/source/css/", self.css_source_folder, False)
    def change_working_dir_to_site_root(self):
        os.chdir("..")

class JavaScript_Concatenator:
    def __init__(self):
        self.js_source_folders = files.remove_unix(os.listdir(dir.js_source_folder)) # dir = Directory_Handler() object instanced at @EOF
        self.concat_js_folders(self.js_source_folders)
    def does_main_js_exist(self, packed_filename, main_js_filepath):
        main_js = pathlib.Path(main_js_filepath)
        if main_js.exists() == False:
            print(packed_filename + " needs a main.js file. Please create one in its folder!")
            exit()
    def concat_js_folders(self, js_source_folder):
        files.delete_directory_contents(dir.js_deploy_folder)
        for folder in js_source_folder:
            folder_filepath = dir.js_source_folder + folder + "/"
            folder_contents = files.remove_unix(os.listdir(folder_filepath))
            packed_filename = folder + ".js"
            packed_filepath = dir.js_deploy_folder + packed_filename
            main_js_filepath = folder_filepath + "main.js"
            self.does_main_js_exist(packed_filename, main_js_filepath)
            main_js_file = open(main_js_filepath, "r")
            files.create_blank_file(packed_filepath)
            packed_file = open(packed_filepath, "a")
            for js_file in folder_contents:
                if js_file != "main.js":
                    js_filepath = dir.js_source_folder + folder + "/" + js_file
                    current_file = open(js_filepath, "r")
                    packed_file.write(current_file.read())
                    packed_file.write("\n\n")
            packed_file.write(main_js_file.read())
            packed_file.close()
            print(folder + ".js has been packed!")
            if js_min == True:
                minifier.minify_js(packed_filename, packed_filepath)

class CSS_Concatenator:
    def __init__(self):
        self.css_source_files = files.remove_unix(os.listdir(dir.css_source_folder))
        self.concat_css_folder(self.css_source_files)
    def concat_css_folder(self, css_source_files):
        files.create_blank_file(dir.packed_css_file)
        packed_css_file = open(dir.packed_css_file, "a")
        for css_file in css_source_files:
            filepath = dir.css_source_folder + css_file
            current_css_file = open(filepath, "r")
            current_heading = "/* " + css_file.capitalize().replace(".css", "") + " styles */"
            packed_css_file.write(current_heading)
            packed_css_file.write("\n\n")
            packed_css_file.write(current_css_file.read())
            packed_css_file.write("\n\n")
            print(css_file + " has been packed!")
        packed_css_file.close()
        if css_min == True:
            minifier.minify_css(dir.packed_css_file)
            print("styles.css has been minified!")

class Minifier:
    def minify_js(self, packed_filename, packed_filepath):
        js_file = open(packed_filepath, "r")
        js_file_contents = js_file.read()
        minified = jsmin(js_file_contents)
        js_file.close()
        js_file = open(packed_filepath, "w")
        js_file.write(minified)
        js_file.close()
        print(packed_filename + " has been minified!")
    def minify_css(self, css_filepath):
        css_file = open(css_filepath, "r")
        css_file_contents = css_file.read()
        css_file.close()
        css_file = open(css_filepath, "w")
        css_file.write(compress(css_file_contents))
        css_file.close()

print("\nWelcome to Webpacker 1.0 by John Micallef\n")
if js_min == True or css_min == True:
    minifier = Minifier()
files = File_Handler()
dir = Directory_Handler()
js_concat = JavaScript_Concatenator()
css_concat = CSS_Concatenator()