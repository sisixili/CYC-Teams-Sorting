module.exports = {
    HOST: "XXX",
    USER: "XXX",
    PASSWORD: "XXX!",
    DB: "cyc",
    dialect: "mysql",
    pool: {
      max: 5, // Max/min number of connections
      min: 0,
      acquire: 30000, // Max time (ms) pool will try to get connection before error
      idle: 10000 // Max time (ms) connection can be idle before release
    }
  };