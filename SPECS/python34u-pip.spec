%global pymajor 3
%global pyminor 4
%global pyver %{pymajor}.%{pyminor}
%global iusver %{pymajor}%{pyminor}u
%global build_wheel 0
%global srcname pip
%global src %(echo %{srcname} | cut -c1)

%if 0%{?build_wheel}
%global python3_wheelname %{srcname}-%{version}-py2.py3-none-any.whl
%endif

Name:           python%{iusver}-%{srcname}
Version:        1.5.6
Release:        1.ius%{?dist}
Summary:        A tool for installing and managing Python %{pyver} packages
Group:          Development/Libraries
License:        MIT
URL:            https://pip.pypa.io
Source0:        https://pypi.python.org/packages/source/%{src}/%{srcname}/%{srcname}-%{version}.tar.gz
Patch0:         allow-stripping-prefix-from-wheel-RECORD-files.patch
BuildArch:      noarch
BuildRequires:  python%{iusver}-devel
BuildRequires:  python%{iusver}-setuptools
%if 0%{?build_wheel}
BuildRequires:  python%{iusver}-pip
BuildRequires:  python%{iusver}-wheel
%endif
Requires:       python%{iusver}-setuptools

%description
Pip is a replacement for `easy_install
<http://peak.telecommunity.com/DevCenter/EasyInstall>`_.  It uses mostly the
same techniques for finding packages, so packages that were made
easy_installable should be pip-installable as well.


%prep
%setup -q -n %{srcname}-%{version}
%patch0 -p1
# fix shebangs
find -name '*.py' -type f -print0 | xargs -0 sed -i '1s|python|&%{pyver}|'


%build
%if 0%{?build_wheel}
%{__python3} setup.py bdist_wheel
%else
%{__python3} setup.py build
%endif


%install
%if 0%{?build_wheel}
pip%{pyver} install --ignore-installed dist/%{python3_wheelname} --root %{buildroot} --strip-file-prefix %{buildroot}
%else
%{__python3} setup.py install --optimize 1 --skip-build --root %{buildroot}
%endif
%{__rm} -f %{buildroot}%{_bindir}/pip


# unfortunately, pip's test suite requires virtualenv >= 1.6 which isn't in
# fedora yet. Once it is, check can be implemented
# tests_require = ['pytest', 'virtualenv>=1.10', 'scripttest>=1.3', 'mock']


%files
%doc LICENSE.txt README.rst docs
%{_bindir}/pip3
%{_bindir}/pip3.4
%{python3_sitelib}/pip*


%changelog
* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 25 2014 Matej Stuchlik <mstuchli@redhat.com> - 1.5.6-1
- Update to 1.5.6

* Fri Apr 25 2014 Matej Stuchlik <mstuchli@redhat.com> - 1.5.4-4
- Rebuild as wheel for Python 3.4

* Thu Apr 24 2014 Matej Stuchlik <mstuchli@redhat.com> - 1.5.4-3
- Disable build_wheel

* Thu Apr 24 2014 Matej Stuchlik <mstuchli@redhat.com> - 1.5.4-2
- Rebuild as wheel for Python 3.4

* Mon Apr 07 2014 Matej Stuchlik <mstuchli@redhat.com> - 1.5.4-1
- Updated to 1.5.4

* Mon Oct 14 2013 Tim Flink <tflink@fedoraproject.org> - 1.4.1-1
- Removed patch for CVE 2013-2099 as it has been included in the upstream 1.4.1 release
- Updated version to 1.4.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 16 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 1.3.1-4
- Fix for CVE 2013-2099

* Thu May 23 2013 Tim Flink <tflink@fedoraproject.org> - 1.3.1-3
- undo python2 executable rename to python-pip. fixes #958377
- fix summary to match upstream

* Mon May 06 2013 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.3.1-2
- Fix main package Summary, it's for Python 2, not 3 (#877401)

* Fri Apr 26 2013 Jon Ciesla <limburgher@gmail.com> - 1.3.1-1
- Update to 1.3.1, fix for CVE-2013-1888.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 09 2012 Tim Flink <tflink@fedoraproject.org> - 1.2.1-2
- Fixing files for python3-pip

* Thu Oct 04 2012 Tim Flink <tflink@fedoraproject.org> - 1.2.1-1
- Update to upstream 1.2.1
- Change binary from pip-python to python-pip (RHBZ#855495)
- Add alias from python-pip to pip-python, to be removed at a later date

* Tue May 15 2012 Tim Flink <tflink@fedoraproject.org> - 1.1.0-1
- Update to upstream 1.1.0

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Oct 22 2011 Tim Flink <tflink@fedoraproject.org> - 1.0.2-1
- update to 1.0.2 and added python3 subpackage

* Wed Jun 22 2011 Tim Flink <tflink@fedoraproject.org> - 0.8.3-1
- update to 0.8.3 and project home page

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Luke Macken <lmacken@redhat.com> - 0.8.2-1
- update to 0.8.2 of pip
* Mon Aug 30 2010 Peter Halliday <phalliday@excelsiorsystems.net> - 0.8-1
- update to 0.8 of pip
* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Jul 7 2010 Peter Halliday <phalliday@excelsiorsystems.net> - 0.7.2-1
- update to 0.7.2 of pip
* Sun May 23 2010 Peter Halliday <phalliday@excelsiorsystems.net> - 0.7.1-1
- update to 0.7.1 of pip
* Fri Jan 1 2010 Peter Halliday <phalliday@excelsiorsystems.net> - 0.6.1.4
- fix dependency issue
* Fri Dec 18 2009 Peter Halliday <phalliday@excelsiorsystems.net> - 0.6.1-2
- fix spec file 
* Thu Dec 17 2009 Peter Halliday <phalliday@excelsiorsystems.net> - 0.6.1-1
- upgrade to 0.6.1 of pip
* Mon Aug 31 2009 Peter Halliday <phalliday@excelsiorsystems.net> - 0.4-1
- Initial package

