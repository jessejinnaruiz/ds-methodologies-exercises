-- USE zillow;
SELECT *
FROM zillow.properties_2016 
LEFT JOIN airconditioningtype ON properties_2016.airconditioningtypeid = airconditioningtype.airconditioningtypeid
LEFT JOIN architecturalstyletype ON properties_2016.architecturalstyletypeid = architecturalstyletype.architecturalstyletypeid
LEFT JOIN buildingclasstype ON properties_2016.buildingclasstypeid = buildingclasstype.buildingclasstypeid
LEFT JOIN heatingorsystemtype ON properties_2016.heatingorsystemtypeid = heatingorsystemtype.heatingorsystemtypeid
LEFT JOIN propertylandusetype ON properties_2016.propertylandusetypeid = propertylandusetype.propertylandusetypeid
LEFT JOIN storytype ON properties_2016.storytypeid = storytype.storytypeid
LEFT JOIN typeconstructiontype ON properties_2016.typeconstructiontypeid = typeconstructiontype.typeconstructiontypeid
INNER JOIN predictions_2016 ON properties_2016.parcelid = predictions_2016.parcelid;



-- SELECT *
-- FROM zillow.properties_2017
-- LEFT JOIN airconditioningtype ON properties_2017.airconditioningtypeid = airconditioningtype.airconditioningtypeid
-- LEFT JOIN architecturalstyletype ON properties_2017.architecturalstyletypeid = architecturalstyletype.architecturalstyletypeid
-- LEFT JOIN buildingclasstype ON properties_2017.buildingclasstypeid = buildingclasstype.buildingclasstypeid
-- LEFT JOIN heatingorsystemtype ON properties_2017.heatingorsystemtypeid = heatingorsystemtype.heatingorsystemtypeid
-- LEFT JOIN propertylandusetype ON properties_2017.propertylandusetypeid = propertylandusetype.propertylandusetypeid
-- LEFT JOIN storytype ON properties_2017.storytypeid = storytype.storytypeid
-- LEFT JOIN typeconstructiontype ON properties_2017.typeconstructiontypeid = typeconstructiontype.typeconstructiontypeid
-- LEFT JOIN predictions_2017 ON properties_2017.parcelid = predictions_2016.parcelid;