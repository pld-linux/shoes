#
Summary:	Ruby runtime and GUI environment
Name:		shoes
Version:	2
Release:	1
License:	Ruby's
Group:		Applications
Source0:	http://shoooes.net/dist/%{name}%{version}.tar.gz
# Source0-md5:	826433cdeb80133899bbb694f7aded8a
URL:		http://shoooes.net/
BuildRequires:	gtk+2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%prep
%setup -q -n %{name}-0.r1134

%build
%{__make} \
	CC="%{__cc}" \
	PREFIX="%{_prefix}"

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with ldconfig}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%endif

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/shoes
%dir %{_libdir}/shoes
%{_libdir}/shoes/VERSION.txt
%dir %{_libdir}/shoes/lib
%attr(755,root,root) %{_libdir}/shoes/lib/binject.so
%{_libdir}/shoes/lib/ftsearch
%attr(755,root,root) %{_libdir}/shoes/lib/ftsearchrt.so
%{_libdir}/shoes/lib/rbconfig
%{_libdir}/shoes/lib/rubygems.rb
%{_libdir}/shoes/lib/rubygems
%{_libdir}/shoes/lib/shoes.rb
%{_libdir}/shoes/lib/shoes
%{_libdir}/shoes/lib/ubygems.rb
%attr(755,root,root) %{_libdir}/shoes/libruby.so
%attr(755,root,root) %{_libdir}/shoes/libruby.so.1.8
%attr(755,root,root) %{_libdir}/shoes/libshoes.so
%{_libdir}/shoes/ruby
%{_libdir}/shoes/samples
%attr(755,root,root) %{_libdir}/shoes/shoes-bin
%attr(755,root,root) %{_libdir}/shoes/shoes.launch
%{_libdir}/shoes/static

#%{_examplesdir}/%{name}-%{version}
