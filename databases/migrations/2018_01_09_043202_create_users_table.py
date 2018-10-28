''' Create table for user info '''
from orator.migrations import Migration


class CreateUsersTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.connection('connection2').create('users') as table:
            table.increments('id')
            table.string('name')
            table.string('email').unique()
            table.string('password')
            table.string('remember_token').nullable()
            table.integer('is_admin').nullable()
            table.timestamps()

            # User profile information
            table.string('user_name').unique()
            table.string('bio', 10485760).nullable()
            table.string('facebook').nullable()
            table.string('twitter').nullable()
            table.string('github').nullable()
            table.string('gitlab').nullable()
            table.string('linkedin').nullable()
            table.string('website').nullable()

            # User Profile Photo
            table.string('image').nullable()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.connection('connection2').drop('users')
