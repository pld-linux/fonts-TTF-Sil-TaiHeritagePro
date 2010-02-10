%define		ver	%(echo %{version} | tr . _)
Summary:	Free TrueType font for Tai Viet script
Summary(pl.UTF-8):	Wolnodostępny font TrueType dla pisma taj viet
Name:		fonts-TTF-Sil-TaiHeritagePro
Version:	2.0
Release:	1
License:	OFL, distributable
Group:		Fonts
# Source0Download: http://scripts.sil.org/cms/SCRIPTs/render_download.php?site_id=nrsi&format=file&media_id=TaiHeritagePro2_0.zip&filename=TaiHeritagePro2_0.zip
Source0:	TaiHeritagePro%{ver}.zip
# Source0-md5:	c8bdd7f921cdca75fff89e8ea1a078fa
URL:		http://scripts.sil.org/cms/SCRIPTs/page.php?site_id=nrsi&item_id=TaiHeritage
BuildRequires:	unzip
Requires(post,postun):	fontpostinst
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		ttffontsdir	%{_fontsdir}/TTF

%description
Padauk is a fully capable Unicode 5.1 font supporting all the Myanmar
characters in the standard. Thus it provides support for minority
languages as well, in both local and Burmese rendering style.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ttffontsdir}
cp -a *.ttf $RPM_BUILD_ROOT%{ttffontsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%doc doc/*
%{ttffontsdir}/TaiHeritagePro.ttf
