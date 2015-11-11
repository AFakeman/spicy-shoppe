from spice import application, manager
import db_fill
#db_fill.update_goods()
manager.run()
application.run(debug = True, use_reloader = False)