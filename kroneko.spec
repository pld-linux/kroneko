Summary:	A KDE3 tool for configuring cron and anacron
Summary(pl):	Narzêdzie KDE3 u³atwiaj±ce konfiguracjê crona i anacrona
Name:		kroneko
Version:	0.3.19
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://kyushu-u.dl.sourceforge.jp/kroneko/5642/%{name}-%{version}.tar.gz
# Source0-md5:	a61ed9e0c09e75af584b9ffcc5ad4489
URL:		http://www.kroneko.bounceme.net/kroneko/eng/
BuildRequires:	fam-devel
BuildRequires:	kdelibs-devel >= 3.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_htmldir	/usr/share/doc/kde/HTML

%description
Kroneko is a KDE3 tool for configuring cron and anacron.

%description -l pl
Kroneko jest narzêdziem KDE3 u³atwiaj±cym konfiguracjê crona
i anacrona.

%prep
%setup -q

%build
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_applnkdir}/Utilities
mv $RPM_BUILD_ROOT%{_applnkdir}/{Applications,Utilities}/kroneko.desktop

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Utilities/*
%{_datadir}/apps/*
%{_pixmapsdir}/*/*/*/*
