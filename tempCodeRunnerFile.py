from flask import Flask
from flask_session import Session
from Controllers.homepage import homepage_bp
from Controllers.masuk import masuk_bp
from Controllers.daftar import daftar_bp
from Controllers.homepage_customer import homepage_customer_bp
from Controllers.keluar import keluar_bp  # Add this import
from Controllers.homepage_merchant import homepage_merchant_bp
from Controllers.profil import profil_bp
from Controllers.berhasil_daftar import berhasil_daftar_bp
from Controllers.gagal_daftar import gagal_daftar_bp
from Controllers.berhasil_masuk import berhasil_masuk_bp
from Controllers.detail_jasa import detail_jasa_bp
from Controllers.pesan_jasa import pesan_jasa_bp
from Controllers.konfirmasi_pesan import konfirmasi_pesan_bp
from Controllers.berhasil_pesan import berhasil_pesan_bp
from Controllers.bayar_pesanan import bayar_pesanan_bp
from Controllers.tambah_jasa import tambahjasa_merch_bp
from Controllers.bantuan_penyedia_jasa import bantuan_penyedia_jasa_bp
from Controllers.detailpesanan_merch import detailpesanan_merch_bp

# Initialize Flask app
app = Flask(__name__, template_folder='Templates', static_folder='Static')

# Session configuration
app.config['SECRET_KEY'] = 'c053d6febe5e4db670ce9c18762de227'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Register blueprints
app.register_blueprint(homepage_bp)
app.register_blueprint(masuk_bp)
app.register_blueprint(daftar_bp)
app.register_blueprint(homepage_customer_bp)
app.register_blueprint(keluar_bp)  # Register the logout blueprint
app.register_blueprint(homepage_merchant_bp)
app.register_blueprint(profil_bp)
app.register_blueprint(berhasil_daftar_bp)
app.register_blueprint(gagal_daftar_bp)
app.register_blueprint(berhasil_masuk_bp)
app.register_blueprint(detail_jasa_bp)
app.register_blueprint(pesan_jasa_bp)
app.register_blueprint(konfirmasi_pesan_bp)
app.register_blueprint(berhasil_pesan_bp)
app.register_blueprint(bayar_pesanan_bp)
app.register_blueprint(tambahjasa_merch_bp)
app.register_blueprint(bantuan_penyedia_jasa_bp)
app.register_blueprint(detailpesanan_merch_bp)

if __name__ == '__main__':
    app.run(debug=True)