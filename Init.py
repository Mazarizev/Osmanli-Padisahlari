from flask import Flask, request
from pymongo import MongoClient
import json

Client = MongoClient ("mongodb://127.0.0.1:27017")
Base = Client ["Ottoman"]
Collection = Base.Sultans

Sultans = [{ "ID": 1, "Name": "Osman", "Number": 1, "Reign": [{ "Start": 1299, "End": 1326 }], "Image": "Osman_I.jpg", "Tughra": "" },
{ "ID": 2, "Name": "Orhan", "Number": 1, "Reign": [{ "Start": 1326, "End": 1362 }], "Image": "Orhan.jpg" , "Tughra": "Orhan_Tughra.JPG" },
{ "ID": 3, "Name": "Murad", "Number": 1, "Reign": [{ "Start": 1362, "End": 1389 }], "Image": "Murad_I.jpg" , "Tughra": "Murad_I_Tughra.png" },
{ "ID": 4, "Name": "Bayezid", "Number": 1, "Reign": [{ "Start": 1389, "End": 1402 }], "Image": "Bayezid_I.jpg" , "Tughra": "Bayezid_I_Tughra.JPG" },
{ "ID": 5, "Name": "Mehmed", "Number": 1, "Reign": [{ "Start": 1413, "End": 1421 }], "Image": "Mehmed_I.jpg" , "Tughra": "Mehmed_I_Tughra.JPG" },
{ "ID": 6, "Name": "Murad", "Number": 2, "Reign": [{ "Start": 1421, "End": 1444 }, { "Start": 1446, "End": 1451 }], "Image": "Murad_II.jpg", "Tughra": "Murad_II_Tughra.JPG" },
{ "ID": 7, "Name": "Mehmed", "Number": 2, "Reign": [{ "Start": 1444, "End": 1446 }, { "Start": 1451, "End": 1481 }], "Image": "Mehmed_II.jpg", "Tughra": "Mehmed_II_Tughra.JPG" },
{ "ID": 8, "Name": "Bayezid", "Number": 2, "Reign": [{ "Start": 1481, "End": 1512 }], "Image": "Bayezid_II.jpg", "Tughra": "Bayezid_II_Tughra.JPG" },
{ "ID": 9, "Name": "Selim", "Number": 1, "Reign": [{ "Start": 1512, "End": 1520 }], "Image": "Selim_I.jpg", "Tughra": "Selim_I_Tughra.JPG" },
{ "ID": 10, "Name": "Suleiman", "Number": 1, "Reign": [{ "Start": 1520, "End": 1566 }], "Image": "Suleiman_I.jpg", "Tughra": "Suleiman_I_Tughra.png" },
{ "ID": 11, "Name": "Selim", "Number": 2, "Reign": [{ "Start": 1566, "End": 1574 }], "Image": "Selim_II.jpg", "Tughra": "Selim_II_Tughra.JPG" },
{ "ID": 12, "Name": "Murad", "Number": 3, "Reign": [{ "Start": 1574, "End": 1595 }], "Image": "Murad_III.jpeg", "Tughra": "Murad_III_Tughra.JPG" },
{ "ID": 13, "Name": "Mehmed", "Number": 3, "Reign": [{ "Start": 1595, "End": 1603 }], "Image": "Mehmed_III.jpg", "Tughra": "Mehmed_III_Tughra.JPG" },
{ "ID": 14, "Name": "Ahmed", "Number": 1, "Reign": [{ "Start": 1603, "End": 1617 }], "Image": "Ahmed_I.jpg", "Tughra": "Ahmed_I_Tughra.JPG" },
{ "ID": 15, "Name": "Mustafa", "Number": 1, "Reign": [{ "Start": 1617, "End": 1618 }, { "Start": 1622, "End": 1623 }], "Image": "Mustafa_I.jpg", "Tughra": "Mustafa_I_Tughra.JPG" },
{ "ID": 16, "Name": "Osman", "Number": 2, "Reign": [{ "Start": 1618, "End": 1622 }], "Image": "Osman_I.jpg" , "Tughra": "Osman_II_Tughra.JPG" },
{ "ID": 17, "Name": "Murad", "Number": 4, "Reign": [{ "Start": 1623, "End": 1640 }], "Image": "Murad_IV.jpg" , "Tughra": "Murad_IV_Tughra.png" },
{ "ID": 18, "Name": "Ibrahim", "Number": 1, "Reign": [{ "Start": 1640, "End": 1648 }], "Image": "Ibrahim.jpg" , "Tughra": "Ibrahim_Tughra.JPG" },
{ "ID": 19, "Name": "Mehmed", "Number": 4, "Reign": [{ "Start": 1648, "End": 1687 }], "Image": "Mehmed_IV.jpg" , "Tughra": "Mehmed_IV_Tughra.JPG" },
{ "ID": 20, "Name": "Suleiman", "Number": 2, "Reign": [{ "Start": 1687, "End": 1691 }], "Image": "Suleiman_II.jpg" , "Tughra": "Suleiman_II_Tughra.JPG" },
{ "ID": 21, "Name": "Ahmed", "Number": 2, "Reign": [{ "Start": 1691, "End": 1695 }], "Image": "Ahmed_II.jpg" , "Tughra": "Ahmed_II_Tughra.JPG" },
{ "ID": 22, "Name": "Mustafa", "Number": 2, "Reign": [{ "Start": 1695, "End": 1703 }], "Image": "Mustafa_II.jpg" , "Tughra": "Mustafa_II_Tughra.JPG" },
{ "ID": 23, "Name": "Ahmed", "Number": 3, "Reign": [{ "Start": 1703, "End": 1730 }], "Image": "Ahmed_III.jpg" , "Tughra": "Ahmed_II_Tughra.JPG" },
{ "ID": 24, "Name": "Mahmud", "Number": 1, "Reign": [{ "Start": 1730, "End": 1754 }], "Image": "Mahmud_I.jpg" , "Tughra": "Mahmud_I_Tughra.JPG" },
{ "ID": 25, "Name": "Osman", "Number": 3, "Reign": [{ "Start": 1754, "End": 1757 }], "Image": "Osman_III.jpg" , "Tughra": "Osman_III_Tughra.JPG" },
{ "ID": 26, "Name": "Mustafa", "Number": 3, "Reign": [{ "Start": 1757, "End": 1774 }], "Image": "Mustafa_III.jpg" , "Tughra": "Mustafa_III_Tughra.JPG" },
{ "ID": 27, "Name": "Abdulhamid", "Number": 1, "Reign": [{ "Start": 1774, "End": 1789 }], "Image": "Abdulhamid_I.jpg" , "Tughra": "Abdulhamid_I_Tughra.JPG" },
{ "ID": 28, "Name": "Selim", "Number": 3, "Reign": [{ "Start": 1789, "End": 1807 }], "Image": "Selim_III.jpg" , "Tughra": "Selim_III_Tughra.JPG" },
{ "ID": 29, "Name": "Mustafa", "Number": 4, "Reign": [{ "Start": 1807, "End": 1808 }], "Image": "Mustafa_IV.jpg" , "Tughra": "Mustafa_IV_Tughra.JPG" },
{ "ID": 30, "Name": "Mahmud", "Number": 2, "Reign": [{ "Start": 1808, "End": 1939 }], "Image": "Mahmud_II.jpg" , "Tughra": "Mahmud_II_Tughra.JPG" },
{ "ID": 31, "Name": "Abdulmejid", "Number": 1, "Reign": [{ "Start": 1839, "End": 1861 }], "Image": "Abdulmejid.jpg" , "Tughra": "Abdulmejid_Tughra.JPG" },
{ "ID": 32, "Name": "Abdulaziz", "Number": 1, "Reign": [{ "Start": 1861, "End": 1876 }], "Image": "Abdulaziz.jpg" , "Tughra": "Abdulaziz_Tughra.JPG" },
{ "ID": 33, "Name": "Murad", "Number": 5, "Reign": [{ "Start": 1876, "End": 1876 }], "Image": "Murad_V.jpg" , "Tughra": "Murad_V_Tughra.JPG" },
{ "ID": 34, "Name": "Abdulhamid", "Number": 2, "Reign": [{ "Start": 1876, "End": 1909 }], "Image": "Abdulhamid_II.jpg" , "Tughra": "Abdulhamid_II_Tughra.png" },
{ "ID": 35, "Name": "Mehmed", "Number": 5, "Reign": [{ "Start": 1909, "End": 1918 }], "Image": "Mehmed_V.png" , "Tughra": "Mehmed_V_Tughra.png" },
{ "ID": 36, "Name": "Mehmed", "Number": 6, "Reign": [{ "Start": 1918, "End": 1922 }], "Image": "Mehmed_VI.jpg", "Tughra": "Mehmed_VI_Tughra.png" }]

Collection.insert (Sultans)