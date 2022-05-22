<template>
  <div class="body">
    <section
      id="hero"
      class="d-flex flex-column justify-content-center align-items-center"
    >
      <div class="container text-center text-md-left" data-aos="fade-up">
        <h1><span>Dunder Mifflin</span>'e Hoşgeldiniz</h1>
        <h2>
          Kalitesi kendi ormanlarımızdan gelen ürünlerimizle doğaya nefes olun.
          Eşsiz dayanıklılığı ve dokusu ile unutmayın ki kağıt bizim işimiz...
        </h2>
        <a href="/store" class="btn-get-started scrollto">Alışverişe Başla</a>
      </div>
    </section>
    <!-- End Hero -->

    <!-- <main id="main"> -->

    <!-- ======= What We Do Section ======= -->
    <section id="what-we-do" class="what-we-do">
      <div class="container">
        <div class="section-title">
          <h2>NEDEN BİZ?</h2>
        </div>

        <div class="row">
          <div class="col-lg-3 col-md-6">
            <div class="icon-box">
              <div class="icon">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="24"
                  height="24"
                  fill="currentColor"
                  class="bi bi-tree-fill"
                  viewBox="0 0 16 16"
                >
                  <path
                    d="M8.416.223a.5.5 0 0 0-.832 0l-3 4.5A.5.5 0 0 0 5 5.5h.098L3.076 8.735A.5.5 0 0 0 3.5 9.5h.191l-1.638 3.276a.5.5 0 0 0 .447.724H7V16h2v-2.5h4.5a.5.5 0 0 0 .447-.724L12.31 9.5h.191a.5.5 0 0 0 .424-.765L10.902 5.5H11a.5.5 0 0 0 .416-.777l-3-4.5z"
                  />
                </svg>
              </div>
              <h4><a>Çevre Dostu</a></h4>
              <p>
                Üretimde,ağaçlarımızı kesmek yerine endüstriyel yetiştirdiğimiz
                ağaçları kullanıyoruz ve kullandığımızın iki katı kadar yeni
                fidanı doğaya kazandırıyoruz.
              </p>
            </div>
          </div>

          <div class="col-lg-3 col-md-6">
            <div class="icon-box">
              <div class="icon">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="24"
                  height="24"
                  fill="currentColor"
                  class="bi bi-bar-chart-line-fill"
                  viewBox="0 0 16 16"
                >
                  <path
                    d="M11 2a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v12h.5a.5.5 0 0 1 0 1H.5a.5.5 0 0 1 0-1H1v-3a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v3h1V7a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v7h1V2z"
                  />
                </svg>
              </div>
              <h4><a>Kalite</a></h4>
              <p>
                Tüm üretim sürecini hassasiyetle sürdürdüğümüz kağıtlarımızın
                kalitesinin tadına varınca başka kağıt kullanamayacaksınız.
              </p>
            </div>
          </div>

          <div class="col-lg-3 col-md-6">
            <div class="icon-box">
              <div class="icon">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="24"
                  height="24"
                  fill="currentColor"
                  class="bi bi-keyboard-fill"
                  viewBox="0 0 16 16"
                >
                  <path
                    d="M0 6a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V6zm13 .25v.5c0 .138.112.25.25.25h.5a.25.25 0 0 0 .25-.25v-.5a.25.25 0 0 0-.25-.25h-.5a.25.25 0 0 0-.25.25zM2.25 8a.25.25 0 0 0-.25.25v.5c0 .138.112.25.25.25h.5A.25.25 0 0 0 3 8.75v-.5A.25.25 0 0 0 2.75 8h-.5zM4 8.25v.5c0 .138.112.25.25.25h.5A.25.25 0 0 0 5 8.75v-.5A.25.25 0 0 0 4.75 8h-.5a.25.25 0 0 0-.25.25zM6.25 8a.25.25 0 0 0-.25.25v.5c0 .138.112.25.25.25h.5A.25.25 0 0 0 7 8.75v-.5A.25.25 0 0 0 6.75 8h-.5zM8 8.25v.5c0 .138.112.25.25.25h.5A.25.25 0 0 0 9 8.75v-.5A.25.25 0 0 0 8.75 8h-.5a.25.25 0 0 0-.25.25zM13.25 8a.25.25 0 0 0-.25.25v.5c0 .138.112.25.25.25h.5a.25.25 0 0 0 .25-.25v-.5a.25.25 0 0 0-.25-.25h-.5zm0 2a.25.25 0 0 0-.25.25v.5c0 .138.112.25.25.25h.5a.25.25 0 0 0 .25-.25v-.5a.25.25 0 0 0-.25-.25h-.5zm-3-2a.25.25 0 0 0-.25.25v.5c0 .138.112.25.25.25h1.5a.25.25 0 0 0 .25-.25v-.5a.25.25 0 0 0-.25-.25h-1.5zm.75 2.25v.5c0 .138.112.25.25.25h.5a.25.25 0 0 0 .25-.25v-.5a.25.25 0 0 0-.25-.25h-.5a.25.25 0 0 0-.25.25zM11.25 6a.25.25 0 0 0-.25.25v.5c0 .138.112.25.25.25h.5a.25.25 0 0 0 .25-.25v-.5a.25.25 0 0 0-.25-.25h-.5zM9 6.25v.5c0 .138.112.25.25.25h.5a.25.25 0 0 0 .25-.25v-.5A.25.25 0 0 0 9.75 6h-.5a.25.25 0 0 0-.25.25zM7.25 6a.25.25 0 0 0-.25.25v.5c0 .138.112.25.25.25h.5A.25.25 0 0 0 8 6.75v-.5A.25.25 0 0 0 7.75 6h-.5zM5 6.25v.5c0 .138.112.25.25.25h.5A.25.25 0 0 0 6 6.75v-.5A.25.25 0 0 0 5.75 6h-.5a.25.25 0 0 0-.25.25zM2.25 6a.25.25 0 0 0-.25.25v.5c0 .138.112.25.25.25h1.5A.25.25 0 0 0 4 6.75v-.5A.25.25 0 0 0 3.75 6h-1.5zM2 10.25v.5c0 .138.112.25.25.25h.5a.25.25 0 0 0 .25-.25v-.5a.25.25 0 0 0-.25-.25h-.5a.25.25 0 0 0-.25.25zM4.25 10a.25.25 0 0 0-.25.25v.5c0 .138.112.25.25.25h5.5a.25.25 0 0 0 .25-.25v-.5a.25.25 0 0 0-.25-.25h-5.5z"
                  />
                </svg>
              </div>
              <h4><a>Yenilikçi</a></h4>
              <p>
                Geleneksel kağıt endüstrisinin aksine üretimde ve satışta en
                güncel teknolojileri sizin için kullanıyoruz.
              </p>
            </div>
          </div>

          <div class="col-lg-3 col-md-6">
            <div class="icon-box">
              <div class="icon">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="32"
                  height="32"
                  fill="currentColor"
                  class="bi bi-headset"
                  viewBox="0 0 16 16"
                >
                  <path
                    d="M8 1a5 5 0 0 0-5 5v1h1a1 1 0 0 1 1 1v3a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1V6a6 6 0 1 1 12 0v6a2.5 2.5 0 0 1-2.5 2.5H9.366a1 1 0 0 1-.866.5h-1a1 1 0 1 1 0-2h1a1 1 0 0 1 .866.5H11.5A1.5 1.5 0 0 0 13 12h-1a1 1 0 0 1-1-1V8a1 1 0 0 1 1-1h1V6a5 5 0 0 0-5-5z"
                  />
                </svg>
              </div>
              <h4><a>Memnuniyet</a></h4>
              <p>
                Bizim için en önemli şey sizin memnuniyetiniz. İstek, öneri,
                şikayet için her zaman bir telefon kadar uzağınızdayız.
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
    <!-- End What We Do Section -->
    <!-- ======= About Section ======= -->
    <section id="about" class="about">
      <div class="container">
        <div class="row">
          <div class="col-lg-6">
            <img src="../assets/img/about.jpg" class="img-fluid" alt="" />
          </div>
          <div class="col-lg-6 pt-4 pt-lg-0">
            <h3>Hakkımızda</h3>
            <p>
              Müşteri memnuniyetini ilke edinmiş olan firmamız, öncelikle
              müşteri odaklı çalışmayı öngören eğitimli elemanlarımızla,
              müşterilerimizin isteklerini doğru bir biçimde algılayıp, bu
              istekler doğrultusunda en uygun çözümü sunmayı hedefleyen ve
              Matbaa firmalarımızın çözüm ortağı olarak sektöründe en iyi
              tedarikçi olma yolunda emin adımlarla ilerlemektedir.
            </p>
            <!-- <ul>
              <li>
                <i class="bx bx-check-double"></i> Ullamco laboris nisi ut
                aliquip ex ea commodo consequat.
              </li>
              <li>
                <i class="bx bx-check-double"></i> Duis aute irure dolor in
                reprehenderit in voluptate velit.
              </li>
            </ul> -->
            <div class="row icon-boxes">
              <div class="col-md-6">
                <i class="bx bx-receipt"></i>
                <h4>
                  Kolay kullanıcı arayüzümüzle artık alışverişleriniz daha
                  kolay!
                </h4>
                <p>
                  Günümüzde müşteriler; kaliteli ürüne sahip olmak istemenin
                  yanında; kolay bir kullanıcı arayüzüne sahip olmak,
                  siparişlerini takip etmek, anlık olarak siparişlerine müdahale
                  etmek, satış sonrası hizmetlerden faydalanmak ve kendilerine
                  özel satış verilerini takip etmek istemektedir.
                </p>
              </div>
              <div class="col-md-6 mt-4 mt-md-0">
                <i class="bx bx-cube-alt"></i>
                <h4>Doğaya zarar vermeden kalitenin tadını çıkarın!</h4>
                <p>
                  Değişen dünya koşulları ve artan farkındalıklar ile birlikte
                  sürdürülebilirlik de müşterilerin karar vermesinde çok önemli
                  bir etken olarak dikkat çekmektedir.Dunder Mifflin bütün bu
                  ihtiyaçlar ve talepler dikkate alınarak geliştirilmiş bir
                  platformdur.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <!-- End About Section -->
    <!-- ======= Services Section ======= -->
    <section id="services" class="services section-bg">
      <div class="container">
        <div class="section-title">
          <h2>Avantajlarımız</h2>
          <!-- <p>Necessitatibus eius consequatur ex aliquid fuga eum quidem</p> -->
        </div>

        <div class="row">
          <div class="col-md-6 mt-4 mt-lg-0">
            <div class="icon-box">
              <!-- icon1 -->
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="32"
                height="32"
                fill="currentColor"
                class="bi bi-recycle"
                viewBox="0 0 16 16"
              >
                <path
                  d="M9.302 1.256a1.5 1.5 0 0 0-2.604 0l-1.704 2.98a.5.5 0 0 0 .869.497l1.703-2.981a.5.5 0 0 1 .868 0l2.54 4.444-1.256-.337a.5.5 0 1 0-.26.966l2.415.647a.5.5 0 0 0 .613-.353l.647-2.415a.5.5 0 1 0-.966-.259l-.333 1.242-2.532-4.431zM2.973 7.773l-1.255.337a.5.5 0 1 1-.26-.966l2.416-.647a.5.5 0 0 1 .612.353l.647 2.415a.5.5 0 0 1-.966.259l-.333-1.242-2.545 4.454a.5.5 0 0 0 .434.748H5a.5.5 0 0 1 0 1H1.723A1.5 1.5 0 0 1 .421 12.24l2.552-4.467zm10.89 1.463a.5.5 0 1 0-.868.496l1.716 3.004a.5.5 0 0 1-.434.748h-5.57l.647-.646a.5.5 0 1 0-.708-.707l-1.5 1.5a.498.498 0 0 0 0 .707l1.5 1.5a.5.5 0 1 0 .708-.707l-.647-.647h5.57a1.5 1.5 0 0 0 1.302-2.244l-1.716-3.004z"
                />
              </svg>

              <!-- <font-awesome-icon icon="fa-solid fa-recycle" class="bi" /> -->
              <h4><a href="#">Geri Dönüşüm</a></h4>
              <p>
                Sıfır atık politikasını benimsediğimiz şirketimizde kullanılmış
                kağıtları getirdiğinizde uyguladığımız indirimler sayesinde
                doğamızı hep beraber koruyoruz.
              </p>
            </div>
          </div>
          <div class="col-md-6 mt-4 mt-lg-0">
            <div class="icon-box">
              <!-- icon1 -->
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="32"
                height="32"
                fill="currentColor"
                class="bi bi-pie-chart-fill"
                viewBox="0 0 16 16"
              >
                <path
                  d="M15.985 8.5H8.207l-5.5 5.5a8 8 0 0 0 13.277-5.5zM2 13.292A8 8 0 0 1 7.5.015v7.778l-5.5 5.5zM8.5.015V7.5h7.485A8.001 8.001 0 0 0 8.5.015z"
                />
              </svg>
              <h4><a href="#">Müşteri Arayüzü</a></h4>
              <p>
                Size özel hazırladığımız kullanıcı arayüzümüz ile
                planlamalarınızı daha kolay yapabileceksiniz.
              </p>
            </div>
          </div>
          <div class="col-md-6 mt-4 mt-lg-0">
            <div class="icon-box">
              <!-- icon1 -->
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="32"
                height="32"
                fill="currentColor"
                class="bi bi-clock-fill"
                viewBox="0 0 16 16"
              >
                <path
                  d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM8 3.5a.5.5 0 0 0-1 0V9a.5.5 0 0 0 .252.434l3.5 2a.5.5 0 0 0 .496-.868L8 8.71V3.5z"
                />
              </svg>
              <h4><a href="#">Hızlı Teslim</a></h4>
              <p>
                Siparişinizi en geç 3 iş günü içinde kargoya vererek beklemeden
                güvenle alışveriş imkanı sunuyoruz.
              </p>
            </div>
          </div>
          <div class="col-md-6 mt-4">
            <div class="icon-box">
              <!-- icon1 -->
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="42"
                height="42"
                fill="currentColor"
                class="bi bi-eyeglasses"
                viewBox="0 0 16 16"
              >
                <path
                  d="M4 6a2 2 0 1 1 0 4 2 2 0 0 1 0-4zm2.625.547a3 3 0 0 0-5.584.953H.5a.5.5 0 0 0 0 1h.541A3 3 0 0 0 7 8a1 1 0 0 1 2 0 3 3 0 0 0 5.959.5h.541a.5.5 0 0 0 0-1h-.541a3 3 0 0 0-5.584-.953A1.993 1.993 0 0 0 8 6c-.532 0-1.016.208-1.375.547zM14 8a2 2 0 1 1-4 0 2 2 0 0 1 4 0z"
                />
              </svg>
              <h4><a href="#">Kolay Takip</a></h4>
              <p>
                Siparişinizi yedi yirmi dört takip edebileceğiniz sipariş takip
                sistemimizle artık online alışveriş daha kolay.
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
    <!-- End Services Section -->
    <section id="testimonials" class="testimonials section-bg">
      <div class="container">
        <div class="section-title">
          <h2>Takımımız</h2>
          <p>
            <i>
              “Talent wins games, but teamwork and intelligence win
              championships”
            </i>
            -Michael Jordan
          </p>
        </div>

        <div class="row">
          <div
            id="carouselExampleIndicators"
            class="carousel slide"
            data-ride="carousel"
          >
            <ol class="carousel-indicators">
              <li
                data-target="#carouselExampleIndicators"
                data-slide-to="0"
                class="active"
              ></li>
              <li
                data-target="#carouselExampleIndicators"
                data-slide-to="1"
              ></li>
              <li
                data-target="#carouselExampleIndicators"
                data-slide-to="2"
              ></li>
            </ol>
            <div class="carousel-inner">
              <div class="carousel-item active">
                <div class="testimonial-item">
                  <p>
                    <i class="bx bxs-quote-alt-left quote-icon-left"></i>
                    Proin iaculis purus consequat sem cure digni ssim donec
                    porttitora entum suscipit rhoncus. Accusantium quam,
                    ultricies eget id, aliquam eget nibh et. Maecen aliquam,
                    risus at semper.
                    <i class="bx bxs-quote-alt-right quote-icon-right"></i>
                  </p>
                  <img
                    src="../assets/img/kerem.jpeg"
                    class="testimonial-img"
                    alt=""
                  />
                  <h3>Kerem Kaya</h3>
                  <h4>Proje Yöneticisi &amp; Front-End Geliştirici</h4>
                </div>
                <!-- <img
                  class="d-block w-100 img-fluid"
                  src="https://placeimg.com/1080/500/animals"
                  alt="First slide"
                />
                <div class="carousel-caption d-none d-md-block">
                  <h5>My Caption Title (1st Image)</h5>
                  <p>
                    The whole caption will only show up if the screen is at
                    least medium size.
                  </p>
                </div> -->
              </div>
              <div class="carousel-item">
                <div class="testimonial-item">
                  <p>
                    <i class="bx bxs-quote-alt-left quote-icon-left"></i>
                    Enim nisi quem export duis labore cillum quae magna enim
                    sint quorum nulla quem veniam duis minim tempor labore quem
                    eram duis noster aute amet eram fore quis sint minim.
                    <i class="bx bxs-quote-alt-right quote-icon-right"></i>
                  </p>
                  <img
                    src="../assets/img/kutaypasa.jpeg"
                    class="testimonial-img"
                    alt=""
                  />
                  <h3>Hasan Kutay Sarı</h3>
                  <h4>Back-End Geliştirici</h4>
                </div>
                <!-- <img
                  class="d-block w-100 img-fluid"
                  src="https://placeimg.com/1080/500/arch"
                  alt="Second slide"
                /> -->
              </div>

              <div class="carousel-item">
                <div class="testimonial-item">
                  <p>
                    <i class="bx bxs-quote-alt-left quote-icon-left"></i>
                    Export tempor illum tamen malis malis eram quae irure esse
                    labore quem cillum quid cillum eram malis quorum velit fore
                    eram velit sunt aliqua noster fugiat irure amet legam anim
                    culpa.
                    <i class="bx bxs-quote-alt-right quote-icon-right"></i>
                  </p>
                  <img
                    src="../assets/img/berkay.jpeg"
                    class="testimonial-img"
                    alt=""
                  />
                  <h3>Berkay Gündüz</h3>
                  <h4>Veri Tabanı Uzmanı &amp; Back-End Geliştirici</h4>
                </div>
                <!-- <img
                  class="d-block w-100 img-fluid"
                  src="https://placeimg.com/1080/500/nature"
                  alt="Third slide"
                /> -->
              </div>

              <div class="carousel-item">
                <div class="testimonial-item">
                  <div class="testimonial-item">
                    <p>
                      <i class="bx bxs-quote-alt-left quote-icon-left"></i>
                      Fugiat enim eram quae cillum dolore dolor amet nulla culpa
                      multos export minim fugiat minim velit minim dolor enim
                      duis veniam ipsum anim magna sunt elit fore quem dolore
                      labore illum veniam.
                      <i class="bx bxs-quote-alt-right quote-icon-right"></i>
                    </p>
                    <img
                      src="../assets/img/aysos.jpeg"
                      class="testimonial-img"
                      alt=""
                    />
                    <h3>Sena Eser</h3>
                    <h4>Sistem Analisti</h4>
                  </div>
                </div>
              </div>

              <div class="carousel-item">
                <div class="testimonial-item">
                  <div class="testimonial-item">
                    <p>
                      <i class="bx bxs-quote-alt-left quote-icon-left"></i>
                      Quis quorum aliqua sint quem legam fore sunt eram irure
                      aliqua veniam tempor noster veniam enim culpa labore duis
                      sunt culpa nulla illum cillum fugiat legam esse veniam
                      culpa fore nisi cillum quid.
                      <i class="bx bxs-quote-alt-right quote-icon-right"></i>
                    </p>
                    <img
                      src="../assets/img/irem.jpeg"
                      class="testimonial-img"
                      alt=""
                    />
                    <h3>İrem Avcı</h3>
                    <h4>İş Geliştirici &amp; Test Uzmanı</h4>
                  </div>
                </div>
              </div>
            </div>
            <a
              class="carousel-control-prev"
              href="#carouselExampleIndicators"
              role="button"
              data-slide="prev"
            >
              <span
                class="carousel-control-prev-icon"
                aria-hidden="true"
              ></span>
              <span class="sr-only">Previous</span>
            </a>
            <a
              class="carousel-control-next"
              href="#carouselExampleIndicators"
              role="button"
              data-slide="next"
            >
              <span
                class="carousel-control-next-icon"
                aria-hidden="true"
              ></span>
              <span class="sr-only">Next</span>
            </a>
          </div>
        </div>
      </div>
    </section>
    <!-- End Testimonials Section -->

    <!------->
    <footer
      v-if="footerStick"
      id="sticky-footer"
      class="flex-shrink-0 py-4 bg-dark text-white-50 fixed-bottom"
    >
      <div class="container text-center" id="footer-part">
        <small>
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="16"
            height="16"
            fill="currentColor"
            class="bi bi-instagram"
            viewBox="0 0 16 16"
          >
            <path
              d="M8 0C5.829 0 5.556.01 4.703.048 3.85.088 3.269.222 2.76.42a3.917 3.917 0 0 0-1.417.923A3.927 3.927 0 0 0 .42 2.76C.222 3.268.087 3.85.048 4.7.01 5.555 0 5.827 0 8.001c0 2.172.01 2.444.048 3.297.04.852.174 1.433.372 1.942.205.526.478.972.923 1.417.444.445.89.719 1.416.923.51.198 1.09.333 1.942.372C5.555 15.99 5.827 16 8 16s2.444-.01 3.298-.048c.851-.04 1.434-.174 1.943-.372a3.916 3.916 0 0 0 1.416-.923c.445-.445.718-.891.923-1.417.197-.509.332-1.09.372-1.942C15.99 10.445 16 10.173 16 8s-.01-2.445-.048-3.299c-.04-.851-.175-1.433-.372-1.941a3.926 3.926 0 0 0-.923-1.417A3.911 3.911 0 0 0 13.24.42c-.51-.198-1.092-.333-1.943-.372C10.443.01 10.172 0 7.998 0h.003zm-.717 1.442h.718c2.136 0 2.389.007 3.232.046.78.035 1.204.166 1.486.275.373.145.64.319.92.599.28.28.453.546.598.92.11.281.24.705.275 1.485.039.843.047 1.096.047 3.231s-.008 2.389-.047 3.232c-.035.78-.166 1.203-.275 1.485a2.47 2.47 0 0 1-.599.919c-.28.28-.546.453-.92.598-.28.11-.704.24-1.485.276-.843.038-1.096.047-3.232.047s-2.39-.009-3.233-.047c-.78-.036-1.203-.166-1.485-.276a2.478 2.478 0 0 1-.92-.598 2.48 2.48 0 0 1-.6-.92c-.109-.281-.24-.705-.275-1.485-.038-.843-.046-1.096-.046-3.233 0-2.136.008-2.388.046-3.231.036-.78.166-1.204.276-1.486.145-.373.319-.64.599-.92.28-.28.546-.453.92-.598.282-.11.705-.24 1.485-.276.738-.034 1.024-.044 2.515-.045v.002zm4.988 1.328a.96.96 0 1 0 0 1.92.96.96 0 0 0 0-1.92zm-4.27 1.122a4.109 4.109 0 1 0 0 8.217 4.109 4.109 0 0 0 0-8.217zm0 1.441a2.667 2.667 0 1 1 0 5.334 2.667 2.667 0 0 1 0-5.334z"
            />
          </svg>
          Instagram: @dundermifflin
        </small>
        <small>
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="16"
            height="16"
            fill="currentColor"
            class="bi bi-twitter"
            viewBox="0 0 16 16"
          >
            <path
              d="M5.026 15c6.038 0 9.341-5.003 9.341-9.334 0-.14 0-.282-.006-.422A6.685 6.685 0 0 0 16 3.542a6.658 6.658 0 0 1-1.889.518 3.301 3.301 0 0 0 1.447-1.817 6.533 6.533 0 0 1-2.087.793A3.286 3.286 0 0 0 7.875 6.03a9.325 9.325 0 0 1-6.767-3.429 3.289 3.289 0 0 0 1.018 4.382A3.323 3.323 0 0 1 .64 6.575v.045a3.288 3.288 0 0 0 2.632 3.218 3.203 3.203 0 0 1-.865.115 3.23 3.23 0 0 1-.614-.057 3.283 3.283 0 0 0 3.067 2.277A6.588 6.588 0 0 1 .78 13.58a6.32 6.32 0 0 1-.78-.045A9.344 9.344 0 0 0 5.026 15z"
            />
          </svg>
          Twitter: @dunder_mifflin
        </small>
        <small
          ><svg
            xmlns="http://www.w3.org/2000/svg"
            width="16"
            height="16"
            fill="currentColor"
            class="bi bi-youtube"
            viewBox="0 0 16 16"
          >
            <path
              d="M8.051 1.999h.089c.822.003 4.987.033 6.11.335a2.01 2.01 0 0 1 1.415 1.42c.101.38.172.883.22 1.402l.01.104.022.26.008.104c.065.914.073 1.77.074 1.957v.075c-.001.194-.01 1.108-.082 2.06l-.008.105-.009.104c-.05.572-.124 1.14-.235 1.558a2.007 2.007 0 0 1-1.415 1.42c-1.16.312-5.569.334-6.18.335h-.142c-.309 0-1.587-.006-2.927-.052l-.17-.006-.087-.004-.171-.007-.171-.007c-1.11-.049-2.167-.128-2.654-.26a2.007 2.007 0 0 1-1.415-1.419c-.111-.417-.185-.986-.235-1.558L.09 9.82l-.008-.104A31.4 31.4 0 0 1 0 7.68v-.123c.002-.215.01-.958.064-1.778l.007-.103.003-.052.008-.104.022-.26.01-.104c.048-.519.119-1.023.22-1.402a2.007 2.007 0 0 1 1.415-1.42c.487-.13 1.544-.21 2.654-.26l.17-.007.172-.006.086-.003.171-.007A99.788 99.788 0 0 1 7.858 2h.193zM6.4 5.209v4.818l4.157-2.408L6.4 5.209z"
            />
          </svg>
          Youtube: Dunder Mifflin Inc.</small
        >

        <small> Copyright &copy; Dunder Mifflin INC.</small>
      </div>
    </footer>
  </div>
</template>

<script>
// import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
export default {
  data() {
    return { footerStick: false, navbarStick: false };
  },
  components: {},

  created() {
    window.addEventListener("scroll", this.handleScroll);
  },
  destroyed() {
    window.removeEventListener("scroll", this.handleScroll);
  },
  mounted() {},
  methods: {
    handleScroll(event) {
      var navHeight = window.innerHeight - 920;
      // console.log("navHeight : " + navHeight);
      // console.log("windowHeight : " + window.innerHeight);

      if (window.scrollY > navHeight) {
        this.footerStick = true;
      } else {
        this.footerStick = false;
        event;
      }
    },
  },
};
</script>

<style >
/*--------------------------------------------------------------
# General
--------------------------------------------------------------*/
.carousel {
  width: 100%;
  height: 100%;
}
.body {
  font-family: "Open Sans", sans-serif;
  color: #444444;
}

a {
  color: #6e6332db;
  text-decoration: none;
}

a:hover {
  color: #efb631;
  text-decoration: none;
}

h1,
h2,
h3,
h4,
h5,
h6 {
  font-family: "Raleway", sans-serif;
}

/*--------------------------------------------------------------
# Back to top button
--------------------------------------------------------------*/
.back-to-top {
  position: fixed;
  visibility: hidden;
  opacity: 0;
  right: 15px;
  bottom: 15px;
  z-index: 996;
  background: #3498db;
  width: 40px;
  height: 40px;
  border-radius: 4px;
  transition: all 0.4s;
}
.back-to-top i {
  font-size: 28px;
  color: #fff;
  line-height: 0;
}
.back-to-top:hover {
  background: #efb631;
  color: #fff;
}
.back-to-top.active {
  visibility: visible;
  opacity: 1;
}

/*--------------------------------------------------------------
# Header
--------------------------------------------------------------*/
#header {
  height: 70px;
  transition: all 0.5s;
  z-index: 997;
  transition: all 0.5s;
  background: #fff;
  box-shadow: 0px 2px 15px rgba(0, 0, 0, 0.1);
}
#header .logo h1 {
  font-size: 28px;
  margin: 0;
  font-weight: 600;
  letter-spacing: 1px;
  text-transform: uppercase;
  color: #384046;
}
#header .logo h1 a,
#header .logo h1 a:hover {
  color: #384046;
  text-decoration: none;
}
#header .logo img {
  max-height: 40px;
}

/*--------------------------------------------------------------
# Header Social Links
--------------------------------------------------------------*/
.header-social-links {
  margin: 0 0 0 30px;
}
.header-social-links a {
  color: #9ba6af;
  padding-left: 8px;
  display: inline-block;
  line-height: 0px;
  transition: 0.3s;
}
.header-social-links a i {
  line-height: 0;
}
.header-social-links a:hover {
  color: #efb631;
}
@media (max-width: 768px) {
  .header-social-links {
    margin: 0 15px 0 0;
  }
}

/*--------------------------------------------------------------
# Navigation Menu
--------------------------------------------------------------*/
/**
* Desktop Navigation 
*/

/*--------------------------------------------------------------
# Hero Section
--------------------------------------------------------------*/
#hero {
  width: 100%;
  height: 60vh;
  background: url("../assets/img/hero-bg.jpg") center center;
  background-size: cover;
  position: relative;
  margin-top: 0px;
  padding: 0;
}
#hero:before {
  content: "";
  background: rgba(56, 64, 70, 0.7);
  position: absolute;
  bottom: 0;
  top: 0;
  left: 0;
  right: 0;
}

#hero .container {
  z-index: 2;
}
#hero h1 {
  margin: 0 0 10px 0;
  font-size: 48px;
  font-weight: 700;
  line-height: 56px;
  color: #fff;
}
#hero h1 span {
  border-bottom: 4px solid #091239db;
}
#hero h2 {
  color: rgba(255, 255, 255, 0.8);
  margin-bottom: 30px;
  font-size: 24px;
}
#hero .btn-get-started {
  font-family: "Poppins", sans-serif;
  font-weight: 400;
  font-size: 13px;
  letter-spacing: 2px;
  display: inline-block;
  padding: 12px 28px;
  border-radius: 4px;
  transition: ease-in-out 0.3s;
  color: #fff;
  background: #091239db;
  text-transform: uppercase;
}
#hero .btn-get-started:hover {
  background: #25386d;
}
@media (max-width: 992px) {
  #hero {
    height: calc(100vh - 70px);
  }
}
@media (max-width: 768px) {
  #hero h1 {
    font-size: 30px;
    line-height: 36px;
  }
  #hero h2 {
    font-size: 18px;
    line-height: 24px;
    margin-bottom: 30px;
  }
}

/*--------------------------------------------------------------
# Sections General
--------------------------------------------------------------*/
section {
  padding: 60px 0;
}

.section-bg {
  background-color: #f7fbfe;
}

.section-title {
  text-align: center;
  padding-bottom: 30px;
}
.section-title h2 {
  font-size: 32px;
  font-weight: 600;
  margin-bottom: 20px;
  padding-bottom: 20px;
  position: relative;
}
.section-title h2::before {
  content: "";
  position: absolute;
  display: block;
  width: 120px;
  height: 1px;
  background: #ddd;
  bottom: 1px;
  left: calc(50% - 60px);
}
.section-title h2::after {
  content: "";
  position: absolute;
  display: block;
  width: 40px;
  height: 3px;
  background: #efb631;
  bottom: 0;
  left: calc(50% - 20px);
}
.section-title p {
  margin-bottom: 0;
}

/*--------------------------------------------------------------
# What We Do
--------------------------------------------------------------*/

.what-we-do .icon-box {
  text-align: center;
  padding: 30px 20px;
  transition: all ease-in-out 0.3s;
  background: #fff;
}
.what-we-do .icon-box .icon {
  margin: 0 auto;
  width: 64px;
  height: 64px;
  background: #eaf4fb;
  border-radius: 50px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 20px;
  transition: ease-in-out 0.3s;
}
.what-we-do .icon-box .icon .bi {
  color: #efb631;
  font-size: 28px;
}
.what-we-do .icon-box h4 {
  font-weight: 700;
  margin-bottom: 15px;
  font-size: 24px;
}
.what-we-do .icon-box h4 a {
  color: #384046;
  transition: ease-in-out 0.3s;
}
.what-we-do .icon-box p {
  line-height: 24px;
  font-size: 14px;
  margin-bottom: 0;
}
.what-we-do .icon-box:hover {
  border-color: #fff;
  box-shadow: 0px 0 25px 0 rgba(0, 0, 0, 0.1);
}
.what-we-do .icon-box:hover h4 a,
.what-we-do .icon-box:hover .icon i {
  color: #efb631;
}

/*--------------------------------------------------------------
# About
--------------------------------------------------------------*/
.about {
  padding: 10px 0;
}
.about h3 {
  font-weight: 600;
  font-size: 32px;
}
.about ul {
  list-style: none;
  padding: 0;
  font-size: 15px;
}
.about ul li + li {
  margin-top: 10px;
}
.about ul li {
  position: relative;
  padding-left: 26px;
}
.about ul i {
  position: absolute;
  left: 0;
  top: 0;
  font-size: 22px;
  color: #3498db;
}
.about .icon-boxes {
  padding-top: 10px;
}
.about .icon-boxes h4 {
  font-size: 20px;
  font-weight: 700;
  margin-top: 5px;
}
.about .icon-boxes i {
  font-size: 48px;
  color: #3498db;
}
.about .icon-boxes p {
  font-size: 15px;
  color: #848484;
}

/*--------------------------------------------------------------
# Skills
--------------------------------------------------------------*/
.skills .progress {
  height: 60px;
  display: block;
  background: none;
  border-radius: 0;
}
.skills .progress .skill {
  padding: 10px 0;
  margin: 0 0 6px 0;
  text-transform: uppercase;
  display: block;
  font-weight: 600;
  font-family: "Poppins", sans-serif;
  color: #384046;
}
.skills .progress .skill .val {
  float: right;
  font-style: normal;
}
.skills .progress-bar-wrap {
  background: #e8eaec;
}
.skills .progress-bar {
  width: 1px;
  height: 10px;
  transition: 0.9s;
  background-color: #5faee3;
}

/*--------------------------------------------------------------
# Counts
--------------------------------------------------------------*/
.counts {
  background: white;
  padding: 30px 0 40px 0;
}
.counts .count-box {
  padding: 30px 30px 25px 30px;
  width: 100%;
  position: relative;
  text-align: center;
  background: #fff;
}
.counts .count-box i {
  position: absolute;
  top: -25px;
  left: 50%;
  transform: translateX(-50%);
  font-size: 20px;
  background: #3498db;
  padding: 12px;
  color: #fff;
  border-radius: 50px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 48px;
  height: 48px;
}
.counts .count-box span {
  font-size: 36px;
  display: block;
  font-weight: 600;
  color: #124364;
}
.counts .count-box p {
  padding: 0;
  margin: 0;
  font-family: "Raleway", sans-serif;
  font-size: 14px;
}

/*--------------------------------------------------------------
# Services
--------------------------------------------------------------*/
#services {
  background-color: #fff8cc;
}
.services .icon-box {
  padding: 30px;
  border-radius: 6px;

  transition: ease-in-out 0.3s;
}
.services .icon-box .bi {
  float: left;
  color: #efb631;
  font-size: 40px;
  line-height: 0;
}
.services .icon-box h4 {
  margin-left: 70px;
  font-weight: 700;
  margin-bottom: 15px;
  font-size: 18px;
}
.services .icon-box h4 a {
  color: #384046;
  transition: 0.3s;
}
.services .icon-box p {
  margin-left: 70px;
  line-height: 24px;
  font-size: 14px;
}
.services .icon-box:hover {
  box-shadow: 0px 2px 22px rgba(0, 0, 0, 0.08);
}
.services .icon-box:hover h4 a {
  color: #efb631;
}

/*--------------------------------------------------------------
# Portfolio
--------------------------------------------------------------*/
.portfolio {
  padding: 60px 0;
}
.portfolio #portfolio-flters {
  padding: 0;
  margin: 0 0 35px 0;
  list-style: none;
  text-align: center;
}
.portfolio #portfolio-flters li {
  cursor: pointer;
  margin: 0 15px 15px 0;
  display: inline-block;
  padding: 10px 20px;
  font-size: 12px;
  line-height: 20px;
  color: #444444;
  border-radius: 4px;
  text-transform: uppercase;
  background: #fff;
  margin-bottom: 5px;
  transition: all 0.3s ease-in-out;
}
.portfolio #portfolio-flters li:hover,
.portfolio #portfolio-flters li.filter-active {
  background: #efb631;
  color: #fff;
}
.portfolio #portfolio-flters li:last-child {
  margin-right: 0;
}
.portfolio .portfolio-wrap {
  box-shadow: 0px 2px 12px rgba(0, 0, 0, 0.08);
  transition: 0.3s;
}
.portfolio .portfolio-wrap:hover {
  box-shadow: 0px 4px 14px rgba(0, 0, 0, 0.16);
}
.portfolio .portfolio-item {
  position: relative;
  height: 360px;
  overflow: hidden;
}
.portfolio .portfolio-item figure {
  background: #000;
  overflow: hidden;
  height: 240px;
  position: relative;
  border-radius: 4px 4px 0 0;
  margin: 0;
}
.portfolio .portfolio-item figure:hover img {
  opacity: 0.4;
  transition: 0.4s;
}
.portfolio .portfolio-item figure .link-preview,
.portfolio .portfolio-item figure .link-details {
  position: absolute;
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  line-height: 0;
  text-align: center;
  width: 36px;
  height: 36px;
  background: #fff;
  border-radius: 50%;
  transition: all 0.2s linear;
  overflow: hidden;
  font-size: 20px;
}
.portfolio .portfolio-item figure .link-preview i,
.portfolio .portfolio-item figure .link-details i {
  color: #384046;
  line-height: 0;
}
.portfolio .portfolio-item figure .link-preview:hover,
.portfolio .portfolio-item figure .link-details:hover {
  background: #efb631;
}
.portfolio .portfolio-item figure .link-preview:hover i,
.portfolio .portfolio-item figure .link-details:hover i {
  color: #fff;
}
.portfolio .portfolio-item figure .link-preview {
  left: calc(50% - 38px);
  top: calc(50% - 18px);
}
.portfolio .portfolio-item figure .link-details {
  right: calc(50% - 38px);
  top: calc(50% - 18px);
}
.portfolio .portfolio-item figure:hover .link-preview {
  opacity: 1;
  left: calc(50% - 44px);
}
.portfolio .portfolio-item figure:hover .link-details {
  opacity: 1;
  right: calc(50% - 44px);
}
.portfolio .portfolio-item .portfolio-info {
  background: #fff;
  text-align: center;
  padding: 30px;
  height: 90px;
  border-radius: 0 0 3px 3px;
}
.portfolio .portfolio-item .portfolio-info h4 {
  font-size: 18px;
  line-height: 1px;
  font-weight: 700;
  margin-bottom: 18px;
  padding-bottom: 0;
}
.portfolio .portfolio-item .portfolio-info h4 a {
  color: #333;
}
.portfolio .portfolio-item .portfolio-info h4 a:hover {
  color: #efb631;
}
.portfolio .portfolio-item .portfolio-info p {
  padding: 0;
  margin: 0;
  color: #b8b8b8;
  font-weight: 500;
  font-size: 14px;
  text-transform: uppercase;
}

/*--------------------------------------------------------------
# Portfolio Details
--------------------------------------------------------------*/
.portfolio-details {
  padding-top: 0;
}

.portfolio-details .portfolio-info {
  padding: 30px;
  box-shadow: 0px 0 30px rgba(56, 64, 70, 0.08);
}
.portfolio-details .portfolio-info h3 {
  font-size: 22px;
  font-weight: 700;
  margin-bottom: 20px;
  padding-bottom: 20px;
  border-bottom: 1px solid #eee;
}
.portfolio-details .portfolio-info ul {
  list-style: none;
  padding: 0;
  font-size: 15px;
}
.portfolio-details .portfolio-info ul li + li {
  margin-top: 10px;
}
.portfolio-details .portfolio-description {
  padding-top: 30px;
}
.portfolio-details .portfolio-description h2 {
  font-size: 26px;
  font-weight: 700;
  margin-bottom: 20px;
}
.portfolio-details .portfolio-description p {
  padding: 0;
}

/*--------------------------------------------------------------
# Testimonials
--------------------------------------------------------------*/
.testimonials {
  background-color: #fff8cc;
}
.testimonials .testimonial-item {
  box-sizing: content-box;
  padding: 30px 30px 0 30px;
  margin: 30px 15px;
  text-align: center;
  min-height: 350px;
  box-shadow: 0px 2px 12px rgba(0, 0, 0, 0.08);
  background: #fff8cc;
}
.testimonials .testimonial-item .testimonial-img {
  max-width: 30%;
  max-height: 30%;
  /* width: 90px; */
  border-radius: 50%;
  border: 4px solid #fff;
  margin: 0 auto;
}
.testimonials .testimonial-item h3 {
  font-size: 18px;
  font-weight: bold;
  margin: 10px 0 5px 0;
  color: #111;
}
.testimonials .testimonial-item h4 {
  font-size: 14px;
  color: #999;
  margin: 0;
}
.testimonials .testimonial-item .quote-icon-left,
.testimonials .testimonial-item .quote-icon-right {
  color: #e1f0fa;
  font-size: 26px;
}
.testimonials .testimonial-item .quote-icon-left {
  display: inline-block;
  left: -5px;
  position: relative;
}
.testimonials .testimonial-item .quote-icon-right {
  display: inline-block;
  right: -5px;
  position: relative;
  top: 10px;
}
.testimonials .testimonial-item p {
  font-style: italic;
  margin: 0 auto 15px auto;
}
.testimonials .swiper-pagination {
  margin-top: 20px;
  position: relative;
}
.testimonials .swiper-pagination .swiper-pagination-bullet {
  width: 12px;
  height: 12px;
  background-color: #fff;
  opacity: 1;
  border: 1px solid #3498db;
}
.testimonials .swiper-pagination .swiper-pagination-bullet-active {
  background-color: #3498db;
}

/*--------------------------------------------------------------
# Team
--------------------------------------------------------------*/
.team .member {
  text-align: center;
  margin-bottom: 20px;
  box-shadow: 0px 0px 12px 0px rgba(0, 0, 0, 0.1);
  padding: 30px 20px;
  background: #fff;
}
.team .member img {
  max-width: 60%;
  border-radius: 50%;
  margin: 0 0 30px 0;
}
.team .member h4 {
  font-weight: 700;
  margin-bottom: 2px;
  font-size: 18px;
}
.team .member span {
  font-style: italic;
  display: block;
  font-size: 13px;
}
.team .member p {
  padding-top: 10px;
  font-size: 14px;
  font-style: italic;
  color: #aaaaaa;
}
.team .member .social {
  margin-top: 15px;
}
.team .member .social a {
  color: #919191;
  transition: 0.3s;
}
.team .member .social a:hover {
  color: #efb631;
}
.team .member .social i {
  font-size: 18px;
  margin: 0 2px;
}

/*--------------------------------------------------------------
# Contact
--------------------------------------------------------------*/
.contact .info-wrap {
  padding: 30px;
  background: #fff;
  border-radius: 4px;
}
.contact .info i {
  font-size: 20px;
  color: #3498db;
  float: left;
  width: 44px;
  height: 44px;
  background: #eaf4fb;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 50px;
  transition: all 0.3s ease-in-out;
}
.contact .info h4 {
  padding: 0 0 0 60px;
  font-size: 22px;
  font-weight: 600;
  margin-bottom: 5px;
  color: #384046;
}
.contact .info p {
  padding: 0 0 0 60px;
  margin-bottom: 0;
  font-size: 14px;
  color: #65747f;
}
.contact .info:hover i {
  background: #efb631;
  color: #fff;
}
.contact .php-email-form {
  width: 100%;
  padding: 30px;
  background: #fff;
  border-radius: 4px;
}
.contact .php-email-form .form-group {
  padding-bottom: 8px;
}
.contact .php-email-form .validate {
  display: none;
  color: red;
  margin: 0 0 15px 0;
  font-weight: 400;
  font-size: 13px;
}
.contact .php-email-form .error-message {
  display: none;
  color: #fff;
  background: #ed3c0d;
  text-align: left;
  padding: 15px;
  font-weight: 600;
}
.contact .php-email-form .error-message br + br {
  margin-top: 25px;
}
.contact .php-email-form .sent-message {
  display: none;
  color: #fff;
  background: #18d26e;
  text-align: center;
  padding: 15px;
  font-weight: 600;
}
.contact .php-email-form .loading {
  display: none;
  background: #fff;
  text-align: center;
  padding: 15px;
}
.contact .php-email-form .loading:before {
  content: "";
  display: inline-block;
  border-radius: 50%;
  width: 24px;
  height: 24px;
  margin: 0 10px -6px 0;
  border: 3px solid #18d26e;
  border-top-color: #eee;
  -webkit-animation: animate-loading 1s linear infinite;
  animation: animate-loading 1s linear infinite;
}
.contact .php-email-form input,
.contact .php-email-form textarea {
  border-radius: 0;
  box-shadow: none;
  font-size: 14px;
}
.contact .php-email-form input {
  height: 44px;
}
.contact .php-email-form textarea {
  padding: 10px 12px;
}
.contact .php-email-form button[type="submit"] {
  background: #3498db;
  border: 0;
  padding: 10px 24px;
  color: #fff;
  transition: 0.4s;
  border-radius: 4px;
}
.contact .php-email-form button[type="submit"]:hover {
  background: #5faee3;
}
@-webkit-keyframes animate-loading {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
@keyframes animate-loading {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

/*--------------------------------------------------------------
# Breadcrumbs
--------------------------------------------------------------*/
.breadcrumbs {
  padding: 40px 0;
  margin-top: 70px;
}
.breadcrumbs h2 {
  font-size: 26px;
  font-weight: 300;
}
.breadcrumbs ol {
  display: flex;
  flex-wrap: wrap;
  list-style: none;
  padding: 0;
  margin: 0;
  font-size: 15px;
}
.breadcrumbs ol li + li {
  padding-left: 10px;
}
.breadcrumbs ol li + li::before {
  display: inline-block;
  padding-right: 10px;
  color: #4f5a62;
  content: "/";
}
@media (max-width: 768px) {
  .breadcrumbs .d-flex {
    display: block !important;
  }
  .breadcrumbs ol {
    display: block;
  }
  .breadcrumbs ol li {
    display: inline-block;
  }
}

/*--------------------------------------------------------------
# Footer
--------------------------------------------------------------*/
#footer {
  color: #444444;
  font-size: 14px;
  background: #f7fbfe;
}
#footer .footer-top {
  padding: 60px 0 30px 0;
  background: #fff;
}
#footer .footer-top .footer-contact {
  margin-bottom: 30px;
}
#footer .footer-top .footer-contact h4 {
  font-size: 22px;
  margin: 0 0 30px 0;
  padding: 2px 0 2px 0;
  line-height: 1;
  font-weight: 700;
}
#footer .footer-top .footer-contact p {
  font-size: 14px;
  line-height: 24px;
  margin-bottom: 0;
  font-family: "Raleway", sans-serif;
  color: #777777;
}
#footer .footer-top h4 {
  font-size: 16px;
  font-weight: bold;
  color: #444444;
  position: relative;
  padding-bottom: 12px;
}
#footer .footer-top .footer-links {
  margin-bottom: 30px;
}
#footer .footer-top .footer-links ul {
  list-style: none;
  padding: 0;
  margin: 0;
}
#footer .footer-top .footer-links ul i {
  padding-right: 2px;
  color: #3498db;
  font-size: 18px;
  line-height: 1;
}
#footer .footer-top .footer-links ul li {
  padding: 10px 0;
  display: flex;
  align-items: center;
}
#footer .footer-top .footer-links ul li:first-child {
  padding-top: 0;
}
#footer .footer-top .footer-links ul a {
  color: #777777;
  transition: 0.3s;
  display: inline-block;
  line-height: 1;
}
#footer .footer-top .footer-links ul a:hover {
  text-decoration: none;
  color: #efb631;
}
#footer .footer-newsletter {
  font-size: 15px;
}
#footer .footer-newsletter h4 {
  font-size: 16px;
  font-weight: bold;
  color: #444444;
  position: relative;
  padding-bottom: 12px;
}
#footer .footer-newsletter form {
  margin-top: 30px;
  background: #fff;
  padding: 6px 10px;
  position: relative;
  border-radius: 4px;
  text-align: left;
  border: 1px solid #b6daf2;
}
#footer .footer-newsletter form input[type="email"] {
  border: 0;
  padding: 4px 8px;
  width: calc(100% - 100px);
}
#footer .footer-newsletter form input[type="submit"] {
  position: absolute;
  top: 0;
  right: -2px;
  bottom: 0;
  border: 0;
  background: none;
  font-size: 16px;
  padding: 0 20px 2px 20px;
  background: #3498db;
  color: #fff;
  transition: 0.3s;
  border-radius: 0 4px 4px 0;
  box-shadow: 0px 2px 15px rgba(0, 0, 0, 0.1);
}
#footer .footer-newsletter form input[type="submit"]:hover {
  background: #57aae1;
}
#footer .credits {
  padding-top: 5px;
  font-size: 13px;
  color: #444444;
}
#footer .social-links a {
  font-size: 18px;
  display: inline-block;
  background: #3498db;
  color: #fff;
  line-height: 1;
  padding: 8px 0;
  margin-right: 4px;
  border-radius: 50%;
  text-align: center;
  width: 36px;
  height: 36px;
  transition: 0.3s;
}
#footer .social-links a:hover {
  background: #5faee3;
  color: #fff;
  text-decoration: none;
}
</style>