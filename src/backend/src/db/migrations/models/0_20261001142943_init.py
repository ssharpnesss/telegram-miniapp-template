from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "users" (
    "user_id" BIGSERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(64) NOT NULL,
    "username" VARCHAR(32),
    "created_at" TIMESTAMPTZ NOT NULL,
    "updated_at" TIMESTAMPTZ NOT NULL
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztlm1v2jAQx79KlFdM2iqa8LS9A8ZWphWmkj2o02SZxASLxE4Tpy3q+O7zmYQ8AYO+WF"
    "u0V0n+dxeff+fk7kH3uUO86OxrREL9nfagM+wTeVPQX2s6DoJMBUHgqaccY+mhFDyNRIht"
    "IcUZ9iIiJYdEdkgDQTmTKos9D0RuS0fK3EyKGb2JCRLcJWKuEvn5S8qUOeSeROljsEAzSj"
    "ynkCcsj6gDCSgjEstAGXrUHTLxQQXAqlNkcy/2WSkoWIo5Z5soygSoLmEkxILAWiKMYS+Q"
    "arLndHvrtDOXdb65GIfMcOyJ3N6nKNN0hEZjC00GFkL6EbRszoC0TDVSKFxI4c1bwzDNtl"
    "E3W51mo91uduod6avyrZraq3UyGbL1qxS44cfhyIKEuCznusggrFQMFngdpcqS1UFdK0Xo"
    "z3G4vQSpf4m/3FiZf0p7XwFSIatAdgT/RQl8fI88wlwxl4+txh6637pX/YvuVa3VeFVEPE"
    "oshjIB7OIhPxZwPuZRkJMz/DwZm8YBjE1jJ2MwFRnbIQEWCIsq5ffSIqhPtpMuRpZYO0no"
    "WXrzEo+33KAzZt4yORV70FvDy8HE6l5+geX8KLrxFL+uNQCLodRlSa21SmXavET7PrQuNH"
    "jUrsejgcLLI+GGasXMz7rWISccC44Yv0PYyf2EUzWlVvyyAueRVS9G/q/6c6l6yihXdpU9"
    "TBCzRa53gTDF9uIOhw6qWLjBd/lWTb7hlxXMsKtqBnAhzWSg6pKQ2vNto1Zi2Tts4cznSa"
    "atbYPWzinrxAYs47zRbnTMVmMzV22UfePU30enWzlAQ0pHNPdcyAkOUEazeUB3l14727uy"
    "Ffs7fFRHEE7cT5Dueb1+AF3ptZOuspWmJ84EYVua6KfJeLRjbMpCyt2T2kL7rXk0qvwrXg"
    "DtPXABRqFFpkxrl90fZdz9z+NeuffBC3oS/ZM2s9UfEZol8w=="
)
