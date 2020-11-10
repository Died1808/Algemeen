# Public
Python scripts voor bewerken Nederlandse en Vlaamse bodeminformatie

Deze repository bevat files om bodemgegevens afkomstig uit het DINOLoket van TNO of de DOV van Vlaanderen te bewerken en visualiseren.

- loks gef 2.0.py
  - Dit script leest de xy- coordinaten en vormt ze om tot RD-new coordinaten. Werkt alleen binnen de directory waar de GEF-files aanwezig      zijn
- Son_KD_litho_11.2_Chron.py
  - Dit script leest (vrijwel) elke .gef file en vomt ze om tot een bodeminterpretatie op basis van:
    - De k-waarde volgens het algoritme beschreven in http://www.rvde.nl/pdf/Doorlatendheid%20notitie.pdf, deze is opgenomen in de meest linkse kolom in [m/dag]. De verschillende kleuren geven aan of voor de matrix meer dan 1,5,10 of 20 [m/dag] is berekend.
    - De middelste kolom (T) geeft het bodemtype weer zoals deze is bepaald aan de hand van de bodemtype-classificatie in http://www.rvde.nl/pdf/Python_bodemklassen.pdf. Opgemerkt wordt dat dit een benadering is, maar waar deze indeling wordt vergeleken met goed beschreven, nabij gelegen, boringen, de overeenkomsten groot zijn. De kleurkeuze kan vanzelfsprekend in het script worden aangepast. Uiteindelijk blijkt een goede kleurkeuze een van de meest uitdagende aspecten van coderen te zijn.
    - De kolom met de KD- en c-waarden zoals Python deze berekent aan de hand van de k-waarde. Hierbij zijn watervoerende lagen dunner dan 2 meter en waterremmende lagen dunner dan 0,4 meter weggelaten om de figuren overzichtelijk te houden.
   - Kern van dit script is overgenomen uit een door Rob van Putten gepubliceerd (linkedIn/Power of Python) script om GEF-files te lezen. De interpretaties zijn natuurlijk precies dat, een interpretatie. Maar het geeft snel een beeld van de mogelijke ondergrondopbouw. Het script is zo geschreven dat ze alleen werkt binnen de directory waar de GEF-files aanwezig zijn.
   - Het script is uitgebreid met een eerste aanzet tot fine- en coarse-up sequences. De benodigde modules staan in de eerste regels.
