import jinja2
import os


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
compiled_dir = os.path.join(os.path.dirname(__file__), 'compiled')

if not os.path.exists(compiled_dir):
    os.makedirs(compiled_dir)

env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))

def compile_templates():
    for root, dirs, files in os.walk(template_dir):
        for filename in files:
            if filename.endswith('.html'):
                path = os.path.relpath(os.path.join(root, filename), template_dir)
                output_path = os.path.join(compiled_dir, path)
                output_dir = os.path.dirname(output_path)
                if not os.path.exists(output_dir):
                    os.makedirs(output_dir)
                print("Compiling %s" % path)
                template = env.get_template(path)
                with open(output_path, 'w') as f:
                    f.write(template.render())

if __name__ == '__main__':
    compile_templates()