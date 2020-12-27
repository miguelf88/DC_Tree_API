# DC_Tree_API
A simple API for a geoJSON file containing tree data in Washington DC.

There are two endpoints
  `/getAll`
  `/getByParam`
  
`/getAll` returns the entire dataset

`/getByParam` can take two parameters:
  `ward` and `condition`
  Possible values for `ward` are `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`
  Possible values for `condition` are `Fair`, `Good`, `Excellent`, ` `, `Dead`, `Poor`
