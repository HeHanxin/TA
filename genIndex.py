import os
import re
from pathlib import Path
from pathlib import WindowsPath
from typing import Optional, List
 
tree_str = ''

def save_file(tree, filename='tree.txt'):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(tree)

class DirectionTree:
    def __init__(self,
                 direction_name: str = 'WorkingDirection',
                 direction_path: str = '.',
                 ignore_list: Optional[List[str]] = None):
        self.owner: WindowsPath = Path(direction_path)
        self.tree: str = '## Welcome to TA Group Pages\n\n###  Contents\n'
        self.fileSign: str = '- [%s](https://hehanxin.github.io/TA/%path)'
        self.dirSign: str = '- %s'
        self.startDirSign: str = '- ####'
        self.indentSpace: str = '  '
        self.ignore_list = ignore_list

        if ignore_list is None:
            self.ignore_list = []
		
        for validPath in self.owner.iterdir():
            if validPath.is_dir() and not(re.match("^\.", validPath.name)):
                self.tree += self.startDirSign + '  ' + validPath.name.title() + "\n"
                self.direction_ergodic(path_object=validPath, parentDir=validPath.name + '/', n=1)

    def tree_add(self, path_object: WindowsPath, parentDir, n=0):
        line = self.indentSpace * n
        fixedName = path_object.name.replace("_", " ")
        fixedName = re.sub(r'.md$', '', fixedName)
        fixedName = fixedName.title()
        if path_object.is_file():
            fileContent = self.fileSign.replace("%s", fixedName) + '\n'
            fileContent = fileContent.replace('%path', parentDir + path_object.name)
            self.tree += line + fileContent + '\n'
            return False
        elif path_object.is_dir():
            self.tree += line + self.dirSign.replace("%s", fixedName) + '\n'
            return True

    def ignore_judge(self, name: str):
        for item in self.ignore_list:
            if re.fullmatch(item, name):
                return False
        return True

    def direction_ergodic(self, path_object: WindowsPath, parentDir, n=0):
        dir_file: list = list(path_object.iterdir())
        dir_file.sort(key=lambda x: x.name.lower())
        for item in dir_file:
            if self.ignore_judge(item.name):
                if self.tree_add(item, parentDir, n):
                    self.direction_ergodic(item, parentDir + item.name + "/", n + 1)


if __name__ == '__main__':
    tree = DirectionTree(ignore_list=['^.*\.assets$', '\.git', '__pycache__', 'test.+', 'venv', '.+\.whl', '\.idea', '.+\.jpg'])
    save_file(tree.tree, 'index.md')
