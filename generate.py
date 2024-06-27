import yaml
import re
from collections import OrderedDict
import argparse

def generate_html(publications_data, template_file='paper-template.html', group_previous_year=2019, non_preprints_to_include=['conference-papers']):
    data = publications_data
	# written by ChatGPT
    from jinja2 import Environment, FileSystemLoader

    def process_paper(paper):
        # shorten the venue
        short_venue = re.search('\((.*)\)', paper['venue'])
        if short_venue is not None:
            paper['venue'] = short_venue.group(1)

        # remove {} from the title
        paper['title'] = paper['title'].replace('{', '').replace('}', '')
        return paper

    for key in publications_data.keys():
        publications_data[key] = [
            process_paper(paper) for paper in publications_data[key]
        ]

	# Organize papers by year
    # papers_by_year = {'Preprints': publications_data['preprints']}
    papers_by_year = {}
    data = []
    for key in non_preprints_to_include:
        data += publications_data[key]

    for paper in sorted(data, key=lambda paper: paper['year'], reverse=True):
        year = paper['year']
        if year <= group_previous_year:
            year = f'{group_previous_year} and before'
        if year not in papers_by_year:
            papers_by_year[year] = []

        papers_by_year[year].append(paper)

    # Set up the Jinja2 environment and load the template
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(template_file)

    # Render the template with the data
    html_output = template.render(papers_by_year=papers_by_year)
    return html_output

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    functions = {
        'html': generate_html,
    }
    parser.add_argument("--yaml_file", default="publications.yaml")
    args = parser.parse_args()
    args.output_type = "html"
    with open(args.yaml_file) as f:
        publications_data = yaml.safe_load(f)

    function = functions[args.output_type]
    print(function(publications_data))

    file= open("publications-generated.html","w")
    file.write(function(publications_data))
    file.close()
