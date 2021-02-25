# post_crud_token_based
Video of how it going to work is attached:-
Video link :- https://drive.google.com/file/d/17Szt7IJtNH1dBf-LQnTr4psZyq2dc_YO/view?usp=sharing



command I used in video:- 
users created are jaydave and davej

Generated token 89043157435ffbb2c00e993cdb40e81871baa37d for user jaydave
Generated token 439fa6b635c2fce786067f075abddfe2b04f31d8 for user davej



jaydave posts ids = [33]
davej posts ids = [34]



http POST http://localhost:8000/posts/post/ "Authorization: Token 89043157435ffbb2c00e993cdb40e81871baa37d" description="jaydave descrip"

http POST http://localhost:8000/posts/post/ "Authorization: Token 439fa6b635c2fce786067f075abddfe2b04f31d8" description="davej descrip"


http PUT http://localhost:8000/posts/post/33/ "Authorization: Token 89043157435ffbb2c00e993cdb40e81871baa37d" description="updated jaydave descript"

http PUT http://localhost:8000/posts/post/34/ "Authorization: Token 439fa6b635c2fce786067f075abddfe2b04f31d8" description="updated davej descript"



http DELETE http://localhost:8000/posts/post/33/ "Authorization: Token 89043157435ffbb2c00e993cdb40e81871baa37d"

http DELETE http://localhost:8000/posts/post/34/ "Authorization: Token 439fa6b635c2fce786067f075abddfe2b04f31d8"


