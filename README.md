# ls
Implémentation simplifiée de `ls`.


# Exécuter
Pour essayer le script, il suffit d'utiliser le script `ls.py` tel que :
```bash
$ python3 ls.py . -a
tests
ls.py
README.md
.gitignore
ls
```

Commandes disponibles :
- `-a` : inclut les fichiers et dossiers cachés
- `-R` : recherche récursive, descend dans les dossiers
- `-l` : affiche la taille des fichiers
- `-c` : indique le nombre de lignes des fichiers
- `-d` : n'affiche que les dossiers et le nombre de fichiers contenus
- `-r` : inverser l'ordre d'affichage


# Tests
```bash
python3 -m unittest tests/*.py
```
