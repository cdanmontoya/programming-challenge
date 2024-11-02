"""create cellphones table

Revision ID: 52f9c896dd58
Revises: 3b8d8982adad
Create Date: 2024-07-23 21:30:29.717936

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "52f9c896dd58"
down_revision: Union[str, None] = "3b8d8982adad"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    conn = op.get_bind()
    conn.execute(
        sa.text(
            """
        CREATE TABLE cellphones (
            user_id UUID NOT NULL, 
            cellphone VARCHAR(64) NOT NULL,
            PRIMARY KEY (user_id, cellphone),
            FOREIGN KEY(user_id) REFERENCES accounts (id)
        );
        """
        )
    )


def downgrade() -> None:
    conn = op.get_bind()
    conn.execute(sa.text("""DROP TABLE IF EXISTS cellphones;"""))
