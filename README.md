# HY tsoha 2018: henkilökohtaisen meemiarkiston modernisointi, nk. meemiarkisto

https://tsoha-python-meemiarkisto.herokuapp.com

Projekti käyttää kuvamateriaalina omaa henkilökohtaista meemiarkistoa.
Projektin tarkoitus on tehdä perinteisestä nginx-tiedostolistausarkistosta modernimpi kuvasivusto jossa kuvia voi selailla helposti.

Suunniteltuja käyttötapauksia:

* Käyttäjä voi lisätä arkistoon kuvia

* Kuville voi lisätä kommentteja

* Kuville voi antaa pisteitä

* Käyttäjäkohtainen kirjautuminen

* ~~Käyttäjillä on upvote/downvote-historia ja kommenttihistoria~~

* Erillinen admin-käyttäjä, joka voi moderoida käyttäjien kommentteja ja bannata käyttäjiä

* Meemin yhteenvetosivu, joka näyttää kuvan, pisteet, kommentit ja käyttäjän (yhteenvetokysely tauluista Meme, User, Comment)

Tarkempi käyttötapauksien status löytyy User stories-osiosta.

## Asennusohjeet lokaalia testaamista varten:

* Kloonaa Git-repositorio git@github.com:Kargamborgh/meemiarkisto.git
* Olettaen että käytössäsi on Python3 ja pip, asenna pip-vaatimukset (pip install -r requirements.txt)
* Käynnistä virtuaaliympäristö (source venv/bin/activate, Windows-ympäristössä "source venv/Scripts/activate)
* Käynnistä sovellus (python run.py)
* Sovellus toimii oletuksena osoitteessa http://localhost:5000

[Tietokantakaavion hahmotelma vko2](https://github.com/Kargamborgh/meemiarkisto/blob/master/documentation/db_sketch_wk2.jpg)

[Tietokantakaavion hahmotelma vko4](https://github.com/Kargamborgh/meemiarkisto/blob/master/documentation/db_sketch_wk4.jpg)

[Tietokantakaavion hahmotelma vko6](https://github.com/Kargamborgh/meemiarkisto/blob/master/documentation/db_sketch_wk6.jpg)

[User stories](https://github.com/Kargamborgh/meemiarkisto/blob/master/documentation/user_stories.md)