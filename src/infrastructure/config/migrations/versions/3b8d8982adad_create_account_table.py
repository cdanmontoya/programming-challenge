"""create account table

Revision ID: 3b8d8982adad
Revises: 
Create Date: 2024-07-23 16:52:39.734213

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "3b8d8982adad"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    conn = op.get_bind()
    conn.execute(
        sa.text(
            """
    CREATE TABLE accounts (
    id UUID NOT NULL,
    email VARCHAR(64) NOT NULL,
    PRIMARY KEY (id));
    """
        )
    )


def downgrade() -> None:
    conn = op.get_bind()
    conn.execute(sa.text("DROP TABLE accounts;"))
