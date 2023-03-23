db.createUser(
    {
        user: "root",
        pwd: "admin#afifa",
        roles: [
            {
                role: "readWrite",
                db: "test_afifa"
            }
        ]
    }
);
