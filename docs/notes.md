# Notes

## run.py
Από αυτό το αρχείο τρέχει η εφαρμογή. Όλα τα υπόλοιπα αρχεία συνδέονται με αυτό.

## requirements.txt
Σε αυτό το αρχείο είναι δηλωμένες όλες οι βιβλιοθήκες

## docker-compose.yml, Dockerfile
Αρχεία που χρειάζεται για να τρέξει το Docker. Άν δεν χρησιμοποιείτε docker αγνοήστε τα

## fotographia.toml .vscode .pre-commit-config.yaml .flake8
Αρχεία που είναι configured το black. Είναι για να γίνεται lint ο κώδικας και να είναι καθαρός

## internal
Σε αυτόν τον φάκελο είναι η βασική λειτουργικότητα της εφαρμογής.

### init.py
Σε αυτό το αρχείο θα κάνουμε import τις functions που θα δημιουργούμε στους φακέλους lib και views

### app.py
Σε αυτό το αρχείο δηλώνουμε την εφαρμογή

### lib
Σε αυτό το φάκελο θα μπαίνουν όλες οι functions που έχουν να κάνουν 
με την επεξεργασία εικονών. π.χ.

```python
def resize(image)
    resized_image = blahblahblah()
    return resized_image
```

Ο σκοπός είναι να τις κάνουμε import στον φάκελο views και να τις 
χρησιμοποιούμε στο REST API.

### views
Σε αυτόν τον φάκελο υπάρχουν τα views και τα routes της εφαρμογής. Κάνουμε import
τις functions από τον φάκελο lib για να φτιάξουμε τα endpoints. π.χ.

```python
from internal.lib.resize import resize

@app.route('/api/resize)
def resize_ep():
    ...
    ...
    return ...
```

Note: Τα endpoints θα είναι πάντα της μορφής '/api/functionallity'

### utils
Σε αυτόν τον φάκελο θα μπαίνουμε διάφορες helper functions που
πιθανόν να χρειαστόυμε. Θα λειτουργήσει σαν συμπλήρωμα του φάκελου lib

### static
Στον φάκελο static θα υπάρχουν τα static αρχεία της εφαρμογής πχ JavaScript, CSS

### templates
Σε αυτόν τον φάκελο θα υπάρχουν τα HTML αρχεία της εφαρμογής