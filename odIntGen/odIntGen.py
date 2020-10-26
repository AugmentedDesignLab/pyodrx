from threeWayIntersection import ThreeWayIntersection
import yaml

# process inputs. From https://stackoverflow.com/questions/1773805/how-can-i-parse-a-yaml-file-in-python
with open("scenario.yaml", 'r') as stream:
    try:
        data = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

angles = []
for i in data:
    angles.append(data[i]['angle'])

intersection = ThreeWayIntersection(angles)
intersection.generate()
