"""Added groups

Revision ID: 383f2a446942
Revises: ef932b2ad2b3
Create Date: 2022-10-13 16:42:39.062919

"""
import sqlalchemy as sa
import sqlmodel
from alembic import op

# revision identifiers, used by Alembic.
revision = "383f2a446942"
down_revision = "ef932b2ad2b3"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "groups",
        sa.Column("name", sqlmodel.sql.sqltypes.AutoString(length=32), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_groups_name"), "groups", ["name"], unique=True)
    op.create_table(
        "users_groups",
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("group_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["group_id"],
            ["groups.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("user_id", "group_id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("users_groups")
    op.drop_index(op.f("ix_groups_name"), table_name="groups")
    op.drop_table("groups")
    # ### end Alembic commands ###
