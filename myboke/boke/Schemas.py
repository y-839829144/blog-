import coreapi
import coreschema
from rest_framework.schemas import AutoSchema, ManualSchema

token_field = coreapi.Field(
                name="Authorization",
                required=False,
                location="header",
                schema=coreschema.String(),
                description="格式：JWT 值",
        )
TokenSchema = AutoSchema([
                token_field
        ]
)


BlogListSchema = AutoSchema([
    # token_field,
    coreapi.Field(
                "id",
                required=False,
                location="query",# form
                schema=coreschema.Integer(),
                # schema=coreschema.String(),
                description="博客ID",
            ),
])
CommentListSchema = AutoSchema([
    # token_field,
    coreapi.Field(
                "blog_id",
                required=False,
                location="query",# form
                schema=coreschema.Integer(),
                # schema=coreschema.String(),
                description="博客ID",
            ),
])